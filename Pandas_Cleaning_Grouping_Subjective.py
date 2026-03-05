import pandas as pd
import numpy as np

data = {
    'transaction_id': range(1, 21),
    'date': pd.date_range('2024-10-01', periods=20, freq='D'),
    'region': ['North', 'South', 'East', 'West', None, 'North', 'South', None, 'East', 'West',
               'North', 'South', 'East', 'West', 'North', None, 'East', 'West', 'North', 'South'],
    'product_category': ['Electronics', 'Clothing', None, 'Books', 'Electronics', 'Home', 
                         'Clothing', 'Books', 'Electronics', None, 'Home', 'Clothing', 
                         'Books', 'Electronics', 'Home', 'Clothing', 'Books', 'Electronics', 
                         'Home', 'Clothing'],
    'sales_amount': [1200, 450, 890, None, 1500, 670, None, 340, 2100, 780, 
                     560, None, 420, 1800, 920, 510, 380, None, 1100, 640],
    'quantity': [2, 5, 3, 1, None, 4, 2, 3, 1, 5, 
                 3, 2, None, 1, 4, 3, 2, 1, None, 4],
    'customer_age': [25, 34, None, 45, 29, None, 38, 52, 27, 41, 
                     33, None, 48, 26, 35, 42, None, 31, 39, 44],
    'payment_method': ['Credit Card', 'UPI', 'Cash', 'Debit Card', 'Credit Card', 
                       'UPI', 'Cash', None, 'Credit Card', 'UPI', 'Debit Card', 
                       'Cash', 'Credit Card', None, 'UPI', 'Cash', 'Debit Card', 
                       'Credit Card', 'UPI', None]
}

df = pd.DataFrame(data)
print(df.info())
print(df.isna().sum())

# df['region'].fillna(df['region'].mode()[0], inplace=True)
df['region'] = df['region'].fillna(df['region'].mode())
df['product_category'] = df['product_category'].fillna(df['product_category'].mode())
df['sales_amount'] = df['sales_amount'].fillna(df['sales_amount'].median())
# df['sales_amount'].fillna(df['sales_amount'].median(),inplace = True)
df['quantity'] = df['quantity'].ffill()
df['customer_age']= df['customer_age'].fillna(round(df['customer_age'].mean()))
df.dropna(subset=['payment_method'], inplace=True)
print(df.isna().sum())

totalsalesbyregion = df.groupby('region')['sales_amount'].sum()
averagesalesyproductcategory = df.groupby('product_category')['sales_amount'].mean()
# groupbybothsalesamount = df.groupby('region','product_category')['sales_amount'].sum()
groupbyboth = df.groupby(['region','product_category'])[['quantity','sales_amount']].sum().reset_index()
displayTopThree = groupbyboth.sort_values(
    by='sales_amount',
    ascending=False
).head(3)
print("Total Sales by Region:\n", totalsalesbyregion)
print("\n\n\nAverage Sales by Category:", averagesalesyproductcategory)
print("\n\n\nRegion-Product Summary:", groupbyboth)
print("\n\n\nTop 3 Region-Product Combinations:", displayTopThree)


def sales_range(sales_amount):
  x= sales_amount.max()- sales_amount.min()
  return x

sales_range_by_each_region = df.groupby('region')['sales_amount'].agg(sales_range)

region_summary = df.groupby('region').agg({
    'sales_amount': ['sum', 'mean', 'max'],
    'quantity': ['sum', 'min']
})

region_summary.columns = [ #making colums from step columns
    'sales_amount_sum',
    'sales_amount_mean',
    'sales_amount_max',
    'quantity_sum',
    'quantity_min'
]

region_summary = region_summary.reset_index()

print("Sales Range by Region:\n", sales_range_by_each_region)
print("\nRegion Summary:\n", region_summary)