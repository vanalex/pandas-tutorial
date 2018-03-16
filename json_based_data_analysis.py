from numpy.random import randn
import numpy as np
import os
import matplotlib.pyplot as plt
import pandas as pd
import json

np.random.seed(123)
plt.rc('figure', figsize=(10, 6))
np.set_printoptions(precision=4)
pd.options.display.max_rows = 20


path = 'data/bitly.txt';

records = [json.loads(line) for line in open(path)]

print('#####records####')
print(records)

time_zones = [rec['tz'] for rec in records if 'tz' in rec]
print('####TIME ZONES####')
print(time_zones)