
import pandas as pd

file_path = "auto.csv"
df = pd.read_csv(file_path, header=None)
print(df)

print(df.columns)

print(df.head(10))

# Cabeceras
headers = ["symboling","normalized-losses","make","fuel-type","aspiration", "num-of-doors","body-style",
         "drive-wheels","engine-location","wheel-base", "length","width","height","curb-weight","engine-type",
         "num-of-cylinders", "engine-size","fuel-system","bore","stroke","compression-ratio","horsepower",
         "peak-rpm","city-mpg","highway-mpg","price"]
print("headers\n", headers)

df.columns = headers
print(df.head(10))

print(df.tail(10))

import numpy as np

# replace "?" to NaN
df.replace("?", np.nan, inplace = True)

df.dropna(subset=["price"], axis=0)

print(df.columns)
df.to_csv("automobile.csv", index=False)