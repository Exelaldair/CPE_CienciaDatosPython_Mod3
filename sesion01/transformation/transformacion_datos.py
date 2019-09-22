# import pandas library
import pandas as pd

# In our case, the Automobile Dataset is an online source,
# and it is in CSV (comma separated value) forma

file_path = "auto.csv"
df = pd.read_csv(file_path, header=None)
#print(df)

# show headers list
print(df.columns)

print(df.head(10))

# create headers list
headers = ["symboling","normalized-losses","make","fuel-type","aspiration", "num-of-doors","body-style",
         "drive-wheels","engine-location","wheel-base", "length","width","height","curb-weight","engine-type",
         "num-of-cylinders", "engine-size","fuel-system","bore","stroke","compression-ratio","horsepower",
         "peak-rpm","city-mpg","highway-mpg","price"]
print("headers\n", headers)

df.columns = headers
print(df.head(10))

print("The last 10 rows of the dataframe\n")
print(df.tail(10))

# we can drop missing values along the column "price" as follows
df.dropna(subset=["price"], axis=0)

# Write your code below and press Shift+Enter to execute
print(df.columns)
df.to_csv("automobile.csv", index=False)

#Basic Insight of Dataset

print(df.dtypes)

# As a result, as shown above, it is clear to see that the data type
# of "symboling" and "curb-weight" are int64, "normalized-losses"
# is object, and "wheel-base" is float64, etc.

print(df.describe())

# describe all the columns in "df"
print(df.describe(include = "all"))


print(df[['length', 'compression-ratio']].describe())
# look at the info of "df"
print(df.info)

