import numpy as np
import pandas as pd

df = pd.read_csv("../data/name.basics.tsv/data.tsv", sep="\t")
# df_cleaned = df.dropna(inplace=True)

print(df.head())
