import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import json
from collections import Counter
import seaborn as sns
from scipy import stats


np.random.seed(123)
plt.rc('figure', figsize=(10, 6))
np.set_printoptions(precision=4)
pd.options.display.max_rows = 20


path = 'data/bitly.txt';

records = [json.loads(line) for line in open(path)]

print('#####records####')
print(records)

# Counting Time Zones in Pure Python
time_zones = [rec['tz'] for rec in records if 'tz' in rec]
print('####TIME ZONES####')
print(time_zones)


def get_counts(sequence):
    counts = {}
    for x in sequence:
        if x in counts:
            counts[x] += 1
        else:
            counts[x] = 1
    return counts


counts = get_counts(time_zones)
print('###COUNTS TIME ZONE###')
print(counts)

print('###COUNTS TIME ZONE NEW YORK###')
print(counts['America/New_York'])
print(len(time_zones))


def top_counts(count_dict, n=10):
    value_key_pairs = [(count, tz) for tz, count in count_dict.items()]
    value_key_pairs.sort()
    return value_key_pairs[-n:]


print('###TOP COUNTS###')
print(top_counts(counts))

counts = Counter(time_zones)
print('###MOST COMMON###')
print(counts.most_common(10))


# Counting Time Zones with pandas
frame = pd.DataFrame(records)
frame.info()
print(frame['tz'][:10])

tz_counts = frame['tz'].value_counts()
print(tz_counts[:10])

clean_tz = frame['tz'].fillna('Missing')
clean_tz[clean_tz == ''] = 'Unknown'
tz_counts = clean_tz.value_counts()
print(tz_counts[:10])

plt.figure(figsize=(10, 4))
subset = tz_counts[:10]
sns.barplot(y=subset.index, x=subset.values)
plt.show()


cframe = frame[frame.a.notnull()]
cframe = cframe.copy()
cframe['os'] = np.where(cframe['a'].str.contains('Windows'),'Windows', 'Not Windows')

print('*****')
print(cframe['os'][:5])


by_tz_os = cframe.groupby(['tz', 'os'])


agg_counts = by_tz_os.size().unstack().fillna(0)

print('*****')
print(agg_counts[:10])


# Use to sort in ascending order
indexer = agg_counts.sum(1).argsort()
print('******')
print(indexer[:10])


count_subset = agg_counts.take(indexer[-10:])
print('count subset')
print(count_subset)

agg_counts.sum(1).nlargest(10)

plt.figure()

# Rearrange the data for plotting
count_subset = count_subset.stack()
count_subset.name = 'total'
count_subset = count_subset.reset_index()
count_subset[:10]
sns.barplot(x='total', y='tz', hue='os',  data=count_subset)


def norm_total(group):
    group['normed_total'] = group.total / group.total.sum()
    return group


results = count_subset.groupby('tz').apply(norm_total)

plt.figure()

sns.barplot(x='normed_total', y='tz', hue='os',  data=results)
plt.show()
g = count_subset.groupby('tz')
results2 = count_subset.total / g.total.transform('sum')
print(results2)