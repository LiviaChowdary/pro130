import csv
import pandas as pd

df=pd.read_csv("final_merged.csv")

print(df.shape)

del df["Luminosity"]
del df["Star_name"]
del df["Distance"]
del df["Mass"]
del df["Radius"]

df.to_csv("cleaned_stars.csv")