import pandas as pd 
data = {"EmployeeID":[201,202,203,204,205,206,207,208,209,210],
        "Name":["Sarah","Michael","Jennifer","David","Lisa","James","Emma","Robert","Sophia","William"],
        "Department":["Engineering","Sales","Marketing","Engineering","HR","Sales","Engineering","Marketing","Sales","HR"],
        "Salary":[85000,62000,71000,92000,58000,68000,78000,75000,65000,60000],
        "Performance Score":[4,3,5,5,4,4,3,4,5,3],
        "Years Of Service":[5,3,7,8,4,6,2,5,4,3]
        }
dataframe1 = pd.DataFrame(data)
print(dataframe1.iloc[5])
print("\n")
dataframe1 =dataframe1.set_index("EmployeeID")
print(dataframe1.loc[208]) 
print("\n")
print(dataframe1[dataframe1["Department"]=="Engineering"])
print("\n")
print(dataframe1[dataframe1["Salary"]>70000])
print("\n")
# salesdep = dataframe1["Department"]=="Sales"
# print(salesdep)
print(dataframe1[(dataframe1['Department'] == 'Sales') & (dataframe1['Performance Score'] >= 4)])
top_3_paid = dataframe1.sort_values(by='Salary', ascending=False).head(3)
print("Top 3 Highest-Paid Employees:")
print(top_3_paid)

sorted_df = dataframe1.sort_values(
    by=['Department', 'Salary'], 
    ascending=[True, False]
)

print("\nSorted by Department and then Salary:")
print(sorted_df)