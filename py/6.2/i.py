import pandas as pd


left, top = map(int, input().split())
right, bottom = map(int, input().split())
df = pd.read_csv('data.csv')
filtered_df = df.query('x >= @left and x <= @right and y >= @bottom and y <= @top')
print(filtered_df)