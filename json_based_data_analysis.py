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

