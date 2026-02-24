import pandas as pd

file_id = "1Mlu9r3afSGz5_02Y3wDJoQLpXszQXaIU"
url = f"https://drive.google.com/uc?export=download&id={file_id}"
df = pd.read_csv(url)
df.set_index('order_id',inplace=True)
print(df.head(),"\n")
print(df.tail(),"\n")

df.info()
# # dataset is having 6 colums and 20 rows
# # quantity and order_date columns is having missing values each having 4 null values
# # order_date column require to convertion we can use
# df['order_date']= pd.to_datetime(df['order_date'])
print(df.info(),"\n")
print(df.describe(),"\n")
# median is 2500
# skwed 
