import pandas as pd
import numpy as np
# day1,task1

# s=pd.Series([1,2,3,4,5])
# print(s)

# # task2
# df=pd.DataFrame({
#     'Name':['Alice','Bob','Charly'],
#     'Age':[24,25,28],
#     'Marks': [89,90,99]})
# print(df)
# print(df.shape)
# print(df.columns)

# # revise task1
# s=pd.Series(range(1,11))
# print(s)

# # task2
# df=pd.DataFrame({
#     'Name':['Alice','Bob','Charly'],
#     'Age':[24,25,28]})
# print(df)
# task3
# data=[
#     ['Tom',24,98],
#     ['Robert',26,90],
#     ['Alice',25,89]
# ]

# df=pd.DataFrame(data,columns=['Name','Age','Score'])
# print(df)

# task4
# df.rename(columns={'Age':'Years','Marks':'Scores'},inplace=True)
# print(df)

# task5
# df['City']=['London','UK','US']
# print(df)
# print(df['Score']**2)

# day 2 task1
# data=[
#     ['Tom',24,98],
#     ['Robert',26,90],
#     ['Alice',25,89]
# ]

# df=pd.DataFrame(data,columns=['Name','Age','Score'])
# print(df)
# df['Name']
# print(df['Name'])
# print(df.iloc[1:3])
# print([df['Age'] > 30])
# revise task1
# data=({
#     'Name':['Alice','Boby','Robert','James'],
#     'Age':[26,30,25,28],
#     'Score':[90,85,98,80],
#     'City':['UK','London','US','Germany'],
#     'Salary':[50000,60000,70000,80000]
# })
# df=pd.DataFrame(data)
# print(df)
# print(df.head(3))
# # task2
# print(df['Name'])
# # task3
# print(df['Age']> 25)
# # task4
# print(df['Salary'].between (50000,80000))

# day3 task1 
# data=({
#     'Name':['Alice','Boby',np.nan,'James'],
#     'Age':[None,30,None,28],
#     'Score':[90,80,98,80],
#     'City':['UK','London','US',np.nan],
#     'Salary':[50000,None,70000,80000]
# })
# df=pd.DataFrame(data)
# print(df)
# # task2
# print(df.drop(columns='Age'))
# # task3
# df['Age']=df['Age'].fillna(df['Age'].mean())
# print(df['Age'])
# # revise task1 
# print(df.notnull())
# # task2
# print(df.fillna(0))
# df['Salary']=df['Salary'].fillna(df['Salary'].mean())
# print(df['Salary'])
# # task3 
# print(df.ffill())

# day 4 task1
# data=({
#     'Employee':['Alice','Boby','Albert','James'],
#     'Age':[24,30,27,28],
#     'Score':[90,80,98,80],
#     'City':['UK','London','US','Germny'],
#     'Salary':[50000,60000,70000,80000],
#     'Depart':['HR', 'IT', 'Finance', 'HR']
# })
# df=pd.DataFrame(data)
# print(df)
# print(df.sort_values(by='Age'))
# print(df.sum(axis=0))
# print(df.describe())
# print(df.sort_values(by='Salary',ascending=False))
# df['Age']=df['Age'].max()
# print(df['Age'])
# print(df['Salary'].mean())
# print(df.sort_values(by=['Depart','Salary'],ascending=False))
# print(df['Salary'].head(3))

# day5 task1
# df1=pd.DataFrame({'Name':['A','B'],'Score':[90,89]})
# df2=pd.DataFrame({'Name':['C','D'],'Score':[86,89]})
# print(pd.concat([df1,df2],axis=0))

# # task2
# df1=pd.DataFrame({'ID':[1,2],'Name':['A','B']})
# df2=pd.DataFrame({'ID':[1,2],'Score':[80,90]})
# res=pd.merge(df1,df2,on='ID',how='outer')
# print(res)

data=({
    'Employee':['Alice','Boby','Albert','James'],
    'Age':[24,30,27,28],
    'Score':[90,80,98,80],
    'City':['UK','London','US','Germny'],
    'Salary':[50000,60000,70000,80000],
    'Depart':['HR', 'IT', 'Finance', 'HR']
})
df=pd.DataFrame(data)
print(df)

s=pd.Series([1,2,3,4,5])

data={
   'Name': ['Alice',np.nan,'Robert','John'],
   'Age':[24,None,27,None],   
   'City':['NY','UK',np.nan,'Lon']

}
df=pd.DataFrame(data)
print(df)
print(df.fillna(0))
df['Age']=df['Age'].fillna(df['Age'].mean())
print(df['Age'])