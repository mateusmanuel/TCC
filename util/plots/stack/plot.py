#!/usr/bin/python

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

df = pd.read_csv('statistics_generation.csv')
df.loc[:,'coverage'] *= 100.0
df.loc[:,'time'] /= 1000.0

# plt.plot(df['seconds'], df['coverage'], linewidth=2.0)
# plt.plot(df['seconds'], df['time'], linewidth=2.0)
# plt.title('Test data generation: Stack with STANDARD_GA')
# plt.xlabel('time (s)')
# plt.ylabel('coverage (%)')
# plt.show()
# fig = plt.gcf()
# fig.savefig('plot.png')

font = {'family' : 'serif',
        'size' : 10 }
plt.rc('font', **font)

fig, ax1 = plt.subplots()
plt.xticks(np.arange(1, 31, step=1))

ax1.plot(df['seconds'], df['coverage'], 'k-', linewidth=2.0)
ax1.set_xlabel('Massa de dados')
# Make the y-axis label, ticks and tick labels match the line color.
ax1.set_ylabel('Cobertura (%)', color='k')
ax1.tick_params('y', colors='k')
ax1.xaxis.set_tick_params(labelsize=7)
# ax1.grid()

ax2 = ax1.twinx()
ax2.plot(df['seconds'], df['time'], 'k--', linewidth=2.0)
ax2.set_ylabel('Esforço computacional (s)', color='k')
ax2.tick_params('y', colors='k')

fig.tight_layout()
fig = plt.gcf()
fig.savefig('stack_generation.png')

plt.show()