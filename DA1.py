import pandas as pd

data = pd.read_csv("new_cases.csv")

"\n"

print(data.head())

"\n"

print(data.shape)

"\n"

print(data.World)

"\n"

print(data['United States'])

"\n"

print(data.iloc[3:11, :])

"\n"

data.World.describe()


