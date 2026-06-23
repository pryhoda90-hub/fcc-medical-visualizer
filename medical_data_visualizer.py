import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# 1
df = pd.read_csv('medical_examination.csv').rename(columns={'sex':'gender'})

# 2
df['overweight'] = ((df.weight / (df.height/ 100) ** 2) > 25).astype('int')

# 3
df.gluc = (df.gluc > 1).astype('int')
df.cholesterol = (df.cholesterol > 1).astype('int') 

# 4
def draw_cat_plot():
    # 5
    df_cat = df.melt(id_vars=['cardio'], value_vars=['cholesterol', 'gluc', 'smoke', 'alco', 'active', 'overweight'])


    # 6
    df_cat = df_cat.groupby(['cardio', 'variable', 'value']).size().reset_index(name='total')
    

    # 7
    graph = sns.catplot(df_cat, x='variable', y='total', col='cardio', kind='bar', hue='value')


    # 8
    fig = graph.fig


    # 9
    fig.savefig('catplot.png')
    return fig


# 10
def draw_heat_map():
    # 11
    df_heat = df[(df['ap_lo'] <= df['ap_hi']) & 
        (df['height'] >= df['height'].quantile(0.025)) & 
        (df['height'] <= df['height'].quantile(0.975)) & 
        (df['weight'] >= df['weight'].quantile(0.025)) & 
        (df['weight'] <= df['weight'].quantile(0.975))]

    # 12
    corr = df_heat.corr()

    # 13
    mask = np.triu(np.ones_like(corr, dtype=bool))



    # 14
    fig, ax = plt.subplots(figsize=(14,6))

    # 15
    sns.heatmap(corr, annot=True, ax=ax, square=True, mask=mask, vmin=-0.08, vmax=0.24, linewidths=0.72, fmt='.1f', center=0, cbar_kws={'ticks': [-.08, 0, .08, .16, .24]})



    # 16
    fig.savefig('heatmap.png')
    return fig
