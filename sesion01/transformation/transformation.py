# import pandas library
import pandas as pd

headers = ["symboling","normalized-losses","make","fuel-type","aspiration", "num-of-doors","body-style",
         "drive-wheels","engine-location","wheel-base", "length","width","height","curb-weight","engine-type",
         "num-of-cylinders", "engine-size","fuel-system","bore","stroke","compression-ratio","horsepower",
         "peak-rpm","city-mpg","highway-mpg","price"]

file_path = "auto.csv"
df = pd.read_csv(file_path, names=headers)

print(df.describe().round(2))

price = df['price'].loc[df['price'] !='?'].count()
print(price)


import numpy as np

# replace "?" to NaN
df.replace("?", np.nan, inplace = True)
df.head(5)

#
missing_data = df.isnull()
print(missing_data.head(5))


for column in missing_data.columns.values.tolist():
    print(column)
    print (missing_data[column].value_counts())
    print("")
