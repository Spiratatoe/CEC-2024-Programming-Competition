import matplotlib
import pandas as pd
import numpy as np
import seaborn as sns

for i in range(1,2):
    data = pd.read_csv("data/helium_data_day_"+ str(3) +".csv")

    df_pivot = data.pivot_table(index='x', 
                            columns='y', 
                            values='value', 
                            aggfunc='mean').sort_index(ascending=False)

    sns.heatmap(df_pivot, cmap='coolwarm')

    matplotlib.pyplot.show()