import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_json('/home/kostya/data-analytics-project-100/ads.json')
df.date_group = pd.to_datetime(df.date_group).dt.date
print(df)

cost_pvt = pd.pivot_table(df,
                          values='cost',
                          index='date_group',
                          aggfunc='sum',
                          dropna=False).reset_index()
cost_pvt.cost = cost_pvt.cost.astype(int)
print(cost_pvt)

fig, ax = plt.subplots(figsize=(18, 6))
plt.plot(cost_pvt['date_group'],
         cost_pvt['cost'],
         color='pink',
         label='ADS cost')

for x, y in zip(cost_pvt.date_group, cost_pvt.cost):
    plt.text(x,
             y,
             int(y) if y > 0 else '',
             fontsize=7,
             fontweight='normal',
             rotation=0,
             ha='center',
             va='center')

ax.set(xlabel='Date',
       ylabel='Cost, RUB',
       title='Picture 09 - Total Ad Campaign Cost')

#Settin up grids and ticks:
plt.grid(axis='both', ls=':', color='grey')
plt.yticks(np.arange(0, 950, 100))
plt.xticks(cost_pvt.date_group[::3])

#Rotate xlabels to 45 deg:
ax.tick_params(axis='x', labelsize=8, labelrotation=45, grid_alpha=0.33)
ax.tick_params(axis='y', labelsize=8, labelright=True, right=True, grid_alpha=0.33)

#Setting up limits for x an y axes:
ax.set_ylim(-50, 950)
xmargin = pd.Timedelta('3D') 
ax.set_xlim(cost_pvt.date_group.min() - xmargin,
            cost_pvt.date_group.max() + xmargin)

#X-ticks - set alignment of rotated labels:
plt.setp(ax.get_xticklabels(), ha='right')

#Auto set of figure's margins
fig.tight_layout()

#plt.legend()
plt.show()
