import pandas as pd
import numpy as np

# part 1
# # empty series
# s=pd.Series()
# print(s)

# s=pd.Series(dtype='int')
# print(s)


# s=pd.Series(dtype='float')
# print(s)

# # series
# data=np.array(['a','b','c','d'])
# s=pd.Series(data)
# print(s)

# data=np.array(['a','b','c','d'])
# s=pd.Series(data,index=[100,101,102,103])
# print(s)

# # series from dictionary

# data={'a':1,'b':2,'c':3}
# s=pd.Series(data)
# print(s)

# data={'a':1,'b':2,'c':3}
# s=pd.Series(data,index=['a','c','d','b',])
# print(s)

# scalar
# s=pd.Series(3,index=[1,2,3,4,5])
# print(s)

# s=pd.Series(3,index=['a','b','c','d'])
# print(s)

# part2:
# acess data from series

# s=pd.Series([1,2,3,4,5],index=['a','b','c','d','e'])
# print(s)

# print(s[0])
# print(s[0:3])
# print(s[2:])
# print(s[-3:])

# labels
# print(s['b'])

# # acces multiple elements
# print(s[['a','b','c']])

# # series arithetic operation
# ser1=pd.Series([1,2,3],index=['usa','Italy','UK'])
# print(ser1)
# ser2=pd.Series([2,4,5,6],index=['usa','Jpan','Germany','UK'])
# print(ser2)

# res=ser1+ser2
# print(res)

# pandas-dataFrame
# df=pd.DataFrame()
# print(df)

# # list
# data=[1,2,3,4,5]
# df=pd.DataFrame(data)
# print(df)

# # list of list
# data=['alex',10],['bob',13],['clara',15]
# df=pd.DataFrame(data,columns=['Name','Age'])
# print(df)

# data frame dictionary of list
# data={'name': ['Tom','Jack','Ricky'],
#       'age':[23,24,21]}
# df=pd.DataFrame(data)
# print(df)

# data frame dictionary of series
# d={'one':pd.Series([1,2,3],
#                    index=['a','b','c']),
#                    'two':pd.Series([1,2,3,4],index=['a','b','c','d'])}
# df=pd.DataFrame(d)
# print(df)

# part 3:
# dataframe selections
# d={'one':pd.Series([1,2,3],index=['a','b','c']),
#    'two':pd.Series([1,2,3,4],index=['a','b','c','d'])}
# df=pd.DataFrame(d)
# print(df)

# print(df['one'])

# print(df[['one','two']])

# add new col dataframe
# d={'one':pd.Series([1,2,3],index=['a','b','c']),
#    'two':pd.Series([1,2,3,4],index=['a','b','c','d'])}
# df=pd.DataFrame(d)
# print(df)
# df['three']=pd.Series([10,20,30],index=['a','b','c'])
# print(df)

# #add new value to perform operation 

# df['four']=df['one']+df['three']
# print(df)

# one or more value access
# df=pd.DataFrame(np.random.randn(5,5),index='A B C D E'.split(),columns='V W X Y Z'.split())
# print(df)

# #row selection
# # loc
# print(df.loc['B'])
# # iloc
# print(df.iloc[2])

# # col selection
# print(df['Y'])

# print(df.loc['B','Y'])

# # MULTIPLE,ROWS AND COL
# print(df.loc[['A','B'],['X','Y']])
# df['new']=df['W']+df['Y']
# df['new1']=[1,2,3,4,5]
# df['new2']=100

# print(df)

# print(df.drop('new2',axis=1))
# # permenantly drop

# print(df.drop('new2',axis=1,inplace=True ))
# print(df)
#    #drop axis 0
# print(df.drop('A',axis=0,inplace=True)) 
# del df['new']
# print(df)

# conditional selection
# df=pd.DataFrame(np.random.randn(5,5),index='A B C D E'.split(),columns='V W X Y Z'.split())
# print(df)

# print(df[df > 0])
# print(df[df < 0])
# print(df[df['W'] > 0])

# # set_index
# print(df.set_index('W'))

# # reset_index
# df=pd.DataFrame(np.random.randn(5,5),index='A C B D E'.split(),columns='V W X Y Z'.split())
# print(df)
# print(df.reset_index())

# part 4
# series and dataframe basic functions

# dtype
# s=pd.Series(np.random.randn(4))
# print("dtype of series:")
# print(s.dtype)

# s=pd.Series(np.random.randint(4))
# print("dtype of series:")
# print(s.dtype)

# #  empty functions
# print("is empty")
# print(s.empty)

# # dim
# print(s.ndim)

# # size
# s=pd.Series(np.random.randn(6))
# print('size of the series')
# print(s.size)

# # head
# s=pd.Series(np.random.randn(10))
# print(s.head(6))

# tale
# s=pd.Series(np.random.randn(15))
# print(s.tail())
# print(s.tail(2))

# # dataFrame
# d={'name':pd.Series(['Tom','Sara','Atlin','Burk']),
#    'age':pd.Series([23,21,25,22]),
#    'rating':pd.Series([3.4,5.1,4.1,2.3])}
# df=pd.DataFrame(d)
# print(df)

# # transpose of df
# print("transpose of df:")
# print(df.T)

# # dtypes
# print(df.dtypes)
# # size
# print(df.size)
# # empty
# print(df.empty)
# # shape
# print(df.shape)  
# # head
# print(df.head(2))
# # tail
# print(df.tail(1))

# statical functions

# d={'name':pd.Series(['Tom','Sara','John','Ann','Maria','Robert','Dav','smith','Bob','Ben']),
#    'age':pd.Series([23,24,25,22,24,26,23,21,22,24]),
#    'rating':pd.Series([3.4,5.1,4.1,2.3,3.9,4.5,3.2,4.8,2.9,3.7])}

# df=pd.DataFrame(d)
# print(df)

# # sum,mean,std
# print(df.sum(numeric_only=True))
# print(df.mean(numeric_only=True))
# print(df.std(numeric_only=True))


# # discribe function
# print(df.describe())

# # 
# df=pd.DataFrame(np.random.randn(6,3),columns=['col1',
#                                               'col2','col3'])
# print(df)
# print(df.rename(columns={'col1':'c1','col2':'c2','col3':'c3'},index={1:'a',2:'b',3:'c'}))

# part5
# sorting
# us_df=pd.DataFrame(np.random.randn(10,2),
#                    index=[1,6,9,4,5,2,0,9,3,4],columns=['col1','col2'])  
# print(us_df)                              #    
# print("sort by index:")
# print(us_df.sort_index())
# print(us_df.sort_index(ascending=False))

# text data
# s=pd.Series(['Tom','James','Robert',np.nan,'STEVE@G','1234'])
# print(s)
# print(s.str.lower())
# print(s.str.upper())

# print(s.str.len())

# print(s.str.split('@'))

# print(s.str.contains('a'))

# missing data handling
# df=pd.DataFrame({'A':[1,2,3,np.nan],
#                  'B':[1,np.nan,np.nan,np.nan]})
# print(df)
# print(df.dropna())
# print(df.fillna(value=5))
# print(df.fillna(value=df['C'].mean()))



# df creation examples
# dict={'name':['John','Mary','Sam','Anna'],
#       'degree':['BA','BBA','BSW','BSC'],
#       'score':[88,90,92,96]}

# df=pd.DataFrame(dict)
# print(df)

# df=pd.DataFrame()
# print(df)

# data=[['tom',10],['jack',12],['ricky',11]]

# df=pd.DataFrame(data,columns=['Name','Age'])
# print(df)

# data=[{'b':2,'c':3},
#       {'a':10,'b':20,'c':30}]

# df=pd.DataFrame(data,index=['first','second'])
# print(df)

# df=pd.DataFrame({'Name':['Tom','jack','anna','krish'],'age':[20,22,21,23]})

# new_df=df[['Name']]
# print(new_df)

# 
# df index
# data={'Name':['John','Anna','Mary','Peter','Robrt'],
#       'Age':[24,25,26,27,28],
#       'Gender':['M','F','M','F','M']}

# df=pd.DataFrame(data)
# print(df.index)

# df_index=df.set_index('Name')
# print(df_index)

# df_reset=df.reset_index()
# print(df_reset)

# row=df_index.loc['John']
# print(row)

# new_index=df.set_index('Age')
# print(new_index)

# access dataframe
# data={'Name':['John','Anna','Mary','Peter','Robrt'],
#        'Age':[24,25,26,27,28],
#        'Gender':['M','F','M','F','M']}
# df=pd.DataFrame(data)
# print(df)

# print(df['Age'])
# print(df.iloc[1])
# subset=df.loc[0:2,['Name','Age']]
# print(subset)
# print(df[df ['Age'] > 25])
# print(df.at[2,'Gender'])

# list=[['Tom',36,75,40000],
#       ['Nick',25,80,25000],
#       ['Krish',30,90,35000],
#       ['Jack',34,43,30000],
#       ['John',29,85,28000]]
# df=pd.DataFrame(list,columns=['Name','Age','Weight','Salary'])
# print(df)
# print(df.iloc[2,3])
# print(df.set_index('Name',inplace=True))

# concatenate
# data1={'Name':['Tom','Nick','Krish','Anuj'],
#        'Age':[23,25,26,24],
#        'Address':['Knnur','Nagpur','Pune','Delhi'],
#        'Qualification':['Msc','Bsc','Mcom','BA']}

# data2={'Name':['Sam','John','Jony','Fionna'],
#        'Age':[27,24,22,26],
#        'Address':['Mumbai','Banglore','Kolkata','Hyd'],
#        'Qualification':['Bcom','BA','Msc','Bsc']}
# df=pd.DataFrame(data1,index=[0,1,2,3])
# df1=pd.DataFrame(data2,index=[4,5,6,7])
# print(df,"\n",df1)
# frame=[df,df1]
# # res=pd.concat(frame)
# # print(res)
# # res2=pd.concat([df,df1], axis=1,join='inner')
# # print(res2)
# res2=pd.concat([df,df1], axis=1,sort=False)
# print(res2)
# # res=pd.concat([df,df1],ignore_index=True)
# # print(res)
# res=pd.concat(frame,keys=['x','y'])
# print(res)

# data1={'Name':['Tom','Nick','Krish','Anuj'],
#        'Age':[23,25,26,24],
#        'Address':['Knnur','Nagpur','Pune','Delhi'],
#        'Qualification':['Msc','Bsc','Mcom','BA']}
# df=pd.DataFrame(data1,index=[0,1,2,3])
# s=pd.Series([1000,2000,3000,4000],name='Salary')
# print(df,"\n",s)
# res=pd.concat([df,s],axis=1)
# print(res)

# merging df
# data1={'key':['k0','k1','k2','k3',],
#     'Name':['Tom','Nick','Krish','Anuj'],
#        'Age':[23,25,26,24],
#        }

# data2={'key':['k0','k1','k2','k3',],
#        'Address':['Knnur','Nagpur','Pune','Delhi'],
#        'Qualification':['Msc','Bsc','Mcom','BA']}
# df=pd.DataFrame(data1)
# df1=pd.DataFrame(data2)
# print(df,"\n",df1)
# res=pd.merge(df,df1,on='key')
# print(res)

# data1={'key1':['k0','k1','k0','k1'],'key':['k0','k1','k2','k3',],
#     'Name':['Tom','Nick','Krish','Anuj'],
#        'Age':[23,25,26,24],
#        }


# data2={'key':['k0','k1','k2','k3',]
#        ,'key1':['k0','k0','k0','k0',],
#        'Address':['Knnur','Nagpur','Pune','Delhi'],
#        'Qualification':['Msc','Bsc','Mcom','BA']}
# df=pd.DataFrame(data1)
# df1=pd.DataFrame(data2)

# print(df,"\n",df1)
# res=pd.merge(df,df1,on=['key','key1'])
# print(res)


# data1={'key1':['k0','k1','k0','k1'],'key':['k0','k1','k2','k3',],
#     'Name':['Tom','Nick','Krish','Anuj'],
#        'Age':[23,25,26,24],
#        }


# data2={'key':['k0','k1','k2','k3',]
#        ,'key1':['k0','k0','k0','k0',],
#        'Address':['Knnur','Nagpur','Pune','Delhi'],
#        'Qualification':['Msc','Bsc','Mcom','BA']}
# df=pd.DataFrame(data1)
# df1=pd.DataFrame(data2)
# print(df,"\n",df1)
# res=pd.merge(df,df1,how='inner',on=['key','key1'])
# print(res)

# join()
# data1={'Name':['Tom','Nick','Krish','Anuj'],
#         'Age':[23,25,26,24]}
        
# data2={'Address':['Knnur','Nagpur','Pune','Delhi'],
#        'Qualification':['Msc','Bsc','Mcom','BA']}

# df=pd.DataFrame(data1,index=['k0','k1','k2','k3'])
# df1=pd.DataFrame(data2,index=['k0','k1','k3','k4'])

# print(df,"\n",df1)
# res=df.join(df1)
# print(res)

# d={'First Score':[100,90,np.nan,95],
#    'Second Score':[30,45,56,np.nan],
#    'Third Score':[np.nan,40,80,98]}
# df=pd.DataFrame(d)
# res=df.isnull()
# print(res)

# data={'Name':['Alex','Bob',np.nan,'Clara'],
#       'Age':[25,np.nan,22,28]}

# df=pd.DataFrame(data)
# print(df.notnull())

# d={'First Score':[100,90,np.nan,95],
#     'Second Score':[30,45,56,np.nan],
#   'Third Score':[np.nan,40,80,98]}
# df=pd.DataFrame(d)
# print(df.fillna(method='bfill'))

# dict={'First Score':[100,90,np.nan,95],
#      'Second Score':[30,45,56,np.nan],
#    'Third Score':[np.nan,40,80,98],
#    'Fourth Score':[np.nan,np.nan,np.nan,65]}
# df=pd.DataFrame(dict)
# print(df.dropna(axis=1))

# reomove duplicates
# data={'Name':['Alice','Rober','Albert','Alice'],
#       'Age':[25,30,35,25],
#       'City':['New York','London','Paris','New York']}
# df=pd.DataFrame(data)
# print('original:')
# print(df)
# dp=df.drop_duplicates()
# print("\nmodified")
# print(dp)

# df=pd.DataFrame({'Name':['Alice','Rober','Albert','Alice'],
#       'Age':[25,30,35,25],
#       'City':['New York','London','Paris','New York']})

# res=df.drop_duplicates(subset=['Name'])
# print(res)

# res=df.drop_duplicates(keep='last')
# print(res)

# res=df.drop_duplicates(keep=False)
# print(res)
# df=df.drop_duplicates(subset=["Name","City"])
# print(df)

# data={'Name':['Alice','Robert','Albert','James','Eve'],
#       'Age':[23,24,25,23,26],
#       'Gender':['F','M','M','F','F'],
#       'Salary': [50000, 55000, 40000, 70000, 48000]}
# df=pd.DataFrame(data)
# df['Age']=df['Age'].astype(float)
# print(df.dtypes)
# df=df.astype({'Age':'float64','Salary': 'str'})


# print(df.dtypes)

# df=pd.DataFrame({'FirstName':['June','Albert','Mary',],
#                  'Gender':['','',''],
#                  'Age':[0,0,0]})
# df['Department'] = np.nan
# print(df)
# # df.dropna(how='all',axis=1,inplace=True)
# # print(df)

# nan_value=float("NaN")
# df.replace(0,nan_value,inplace=True)
# df.replace("",nan_value,inplace=True)
# df.dropna(how='all',axis=1,inplace=True)
# print(df)


# str manipulation
# data={'Name':['Albert','John','Anna','mary',np.nan,'Elena'],
#       'City':['New York','paris','London','new delhi','Berlin','UK']}
# df=pd.DataFrame(data)
# print(df)
# print(df.astype('string'))
# print(df['Name'].str.lower())
# print(df['Name'].str.upper())
# print(df['Name'].str.strip())
# print(df['Name'].str.split('a'))
# print(df['City'].str.len())
# print(df['Name'].str.cat(sep=','))
# print(df['Name'].str.get_dummies())
# print(df['Name'].str.startswith('A'))
# print(df['Name'].str.endswith('a'))
# print(df['Name'].str.replace('Elena','Emma'))
# print(df['Name'].str.repeat(2))
# print(df['Name'].str.find('a'))
# print(df['Name'].str.findall('a'))
# print(df['Name'].str.islower())
# print(df['Name'].str.isupper())
# print(df['Name'].str.isnumeric())
# print(df['Name'].str.swapcase())

# sorting
# data={'Name':['Tom','Alice','Mary','Bob'],
#       'Age':[25,30,23,22],
#       'Score':[85,90,78,92]}

# df=pd.DataFrame(data)
# # sorted_df=df.sort_values(by='Age')
# # sorted_df=df.sort_values(by='Age',ascending=True)
# sorted_df=df.sort_values(by=['Age','Score'])
# print(sorted_df)
# data={'Name':['Alice','Bob','Mary','Tom'],

#       'Age':[28,22,25,22],
#       'Score':[85,90,78,92]}
# df_nan=pd.DataFrame(data)
# sorted_df=df_nan.sort_values(by='Name',key=lambda col: col.str.lower())
# print(sorted_df)

# sorted_df=df_nan.sort_values(by='Age',na_position='first')
# print(sorted_df)
# sorted_index=df_nan.sort_index()
# print(sorted_index)

# sorted_df=df_nan.sort_value(by='Age'kind='heapsort')

# gropuing
# df=pd.DataFrame([[9,4,8,9],
#                  [8,10,7,6],
#                  [7,6,8,5]],
#                  columns=['Maths','Physics','Chemistry','Biology'],)
# print(df)
# print(df.sum())
# print(df.describe())
# print(df.agg(['sum','min','max']))

# data={'Item':['Cake','Breed','Cake','Bread','Pastry'],
#       'Flavour':['vannila','wheat','chocolate','strawberry','butterscotch'],
#       'Price':[250,50,250,60,300]}
# df=pd.DataFrame(data)
# print(df)
# grouped=df.groupby('Item')
# print(grouped)

# print(df.groupby('Item')['Price'].sum())
# print(df.groupby(['Item','Flavour'])['Price'].sum())


# series
# data=np.array(['a','b','c','d'])
# s=pd.Series(data)
# print(s)

# data_list=['a','b','c','d']
# s=pd.Series(data_list)
# print(s)

# data_dict={'a':10,'b':20,'c':30}
# s=pd.Series(data_dict)
# print(s)

# s=pd.Series(np.linspace(1,10,5))
# print(s)

# s=pd.Series(range(1,11))
# print(s)

# s=pd.Series(range(1,20,3),index=[x for x in 'abcdefg'])
# print(s)

# data=np.array(['a','b','c','d','e','f','g','h','i','j'])
# s=pd.Series(data,index=[10,11,12,13,14,15,16,17,18,19])
# print(s[[11,12,13,14,15]])

# s=pd.Series(np.arange(3,9),index=['a','b','c','d','e','f'])
# print(s[['a','d']])

# binary operations
# s1=pd.Series([10,20,30],index=['a','b','c'])
# s2=pd.Series([1,2,3],index=['a','b','c'])

# # print(res)
# # res=s1+s2
# res=s1==s2
# print(res)

# df operations
# df1=pd.DataFrame({'A':[10,20,30],'B':[40,50,60]})
# df2=pd.DataFrame({'A':[15,20,35],'B':[30,5,65]})
# res=df1>df2
# print(res)

# s1=pd.Series([True,False,True])
# s2=pd.Series([False,False,True])
# res=s1&s2
# print(res)
# data=pd.Series([10,20,30,40],index=['a','b','c','d'])
# print("original:",data.index)
# data.index=['w','x','y','z']
# print("modified \n",data)\
# data=np.array(['a','b','c','d'])
# s=pd.Series(data,index=[1000,1001,1002,1003])
# print(s)

# df=pd.DataFrame({
#     'Name':['Alice','Bob','Clara','Alice','Bob'],
#     'Age':[25,30,35,25,None],
#     'City':['NY','LA','NY','NI','LA'],
#     'Score':[85,90,78,88,92]
# })
# print(df)
# print(df.head(3))
# print(df.info())
# print(df[['Name','Score']])
# print(df[df['Age'] > 25])
# print(df.isnull())
# df['Age']=df['Age'].fillna(df['Age'].mean())
# print(df['Age'])
# res=df.sort_values(by='Score',ascending=False)
# print(res)
# print(df.sort_index())
# print(df.duplicated())
# print(df.drop_duplicates(subset=['Name']))
# print(df.groupby('City')['Score'].mean())
# print(df.groupby('City').size())
# df['Score']=df['Score'].apply(lambda x : x + 5)
# print(df['Score'])
# df.columns=df.columns.str.lower()
# print(df.columns)

# data={
#     'Name':['Alice','Robert','Bob','Clara','james'],
#     'Age':[26,28,30,24,None],
#     'City':['New York','London','Los Angeles',np.nan,'Chicago'],
#     'Score':[90,85,88,89,None]
# }
# df=pd.DataFrame(data)
# # 

# df['Score']= df['Score'] * 1.10
# print(df['Score'])

# print(df[['Age','Score']])
# print(df[df['Age'] > 25])
# print(df.loc['Alice'])
# print(df[df['Score'] >=80])
# print(df[(df['City']=='New York') & (df['Age'] < 30)])
# print(df.fillna(0))

# df['Score']=df['Score'].fillna(df['Score'].mean())
# print(df['Score'])
# print(df.dropna)

# print(df.sort_values(by='Age'))
# print(df.sort_values(by='Score',ascending=False))
# print(df.sort_index(key=lambda x : x.str.lower()))
# df['Passed'] = df['Score'] >= 50
# print(df['Passed'])
# df.rename(columns={'Score': 'Marks'},inplace=True)
# print(df)
# df.drop(columns='City',inplace=True)
# print(df)
# data= {
#     'Department' : ['HE','IT','HR','IT'],
#     'Salary':[50000,60000,70000,80000]
# }
# df=pd.DataFrame(data)
# df= df.groupby('Department')['Salary'].mean()
# print(df)
# df1=df.groupby('Department')['Salary'].max()
# print(df1)



# print(df.head(3))
# print(df.shape)
# print(df.columns)
# print(df.dtypes)
# res=df.rename(columns={'Age':'Years'})
# print(res)
# print(df.set_index('Name'))
# print(df.reset_index())
# print(df['Name'],df['Age'])
# print(df['Age'] > 25)
# print(df.filter(['City']))
# print(df[df['City'] == 'Delhi'])
# print(df.iloc[2:4])
# print(df.at[2,'Age'])
# print(df.isnull())
# 12
# print(df.fillna({'Age': df['Age'].mean()}))
# print(df.dropna())
# print(df.drop(columns=['City']))

# print(df.replace({'City':{'NI':'Unknown'}}))
# print(df.sort_values(by=['Age'],ascending=False))
# print(df.sort_values(by=['City','Age'],ascending=[True,False]))

# res=df.groupby('City')['Age'].mean()
# print(res)
# df['Score']=[90,89,95,np.nan,90]
# res1=df.groupby('Score').size
# print(res1)
# res2=df.groupby('Age').agg('mean','max')
# print(res2)

# print(df.drop_duplicates('Name'))
# # print(df.astype('Age',int))
# df['Age_Group'] =[24,30,25,26,31]
# print(df['Age_Group']< 25 )
# print(df['City'].str.upper())

# df1=pd.DataFrame({
#     'ID':[1,2,3,4],
#     'Age':[23,24,25,25]
# })
# df2=pd.DataFrame({'ID':[ 1,2,6,7],
#                   'Age':[23,24,26,28]})
# res=pd.merge(df1,df2, on='ID', how='left')
# print(res)
# print(pd.concat([df1,df2],axis=1))


# data={
#     'Name':['Alice',np.nan,'Bob',np.nan,'Robert'],
#     'Age':[35,None,26,35,None],
#     'City':['London',np.nan,'NY','Paris',np.nan],
#     'Score':[None,90,89,95,80]
# }
# df=pd.DataFrame(data)

# df.rename(columns={'Name': 'Student_Name'},inplace=True)
# print(df)
# df.set_index('Student_Name',inplace=True)
# print(df)
# df.reset_index(inplace=True)
# print(df)







data=[
    ['Tom',22,85],
    ['Jerry',24,90],
    ['Anna',23,88]
]
df=pd.DataFrame(data,columns=['Name','Age','Score'])
print(df)

print(df['Name'])
print(df[['Name','Age']])
print(df.loc[0])
print(df[df['Age'] > 23])
print(df.iloc[0:2,1:3])
df['Passed']= df['Score'] >= 40
print(df)
print(df.drop(columns=['Name']))
