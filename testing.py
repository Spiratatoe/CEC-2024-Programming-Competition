

import pandas as pd
import numpy as np
import seaborn as sns

data = pd.read_csv("data/algal_data_day_1.csv")

df_pivot = data.pivot_table(index='x', 
                          columns='y', 
                          values='value', 
                          aggfunc='mean').sort_index(ascending=False)

sns.heatmap(df_pivot, annot=True, cmap='coolwarm')
