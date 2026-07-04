import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns 



# # day 1 task1 
# y=[2,4,6,8,10]

# plt.plot(y)
# plt.show()

# task2
# x=np.array([1,2,3,4,5])
# y=np.array([10,20,30,40,50])

# plt.scatter(x,y)
# plt.xlabel('x axis')
# plt.ylabel('y axis')
# plt.title('scatter plot')
# plt.show()


# revise task 1
# x=np.arange(1,10)

# plt.plot(x)
# plt.show()

# task 2
# height=np.array([150,158,160,165])
# weight=np.array([38,40,45,50])

# plt.scatter(height,weight)
# plt.xlabel('Height')
# plt.ylabel('Weight')
# plt.title('Height vs Weight')
# plt.show()

# task3
# x=np.random.randn(100)

# plt.hist(x,bins= 20)
# plt.title('Histogram')
# plt.show()

# day 2 task 1
# df=pd.DataFrame({
#     'Age':[22,25,27,30,32,35,40,45]
# })
# sns.kdeplot(x='Age',data=df)

# plt.title('Kde plot')
# plt.show()

# task 2
# df=pd.DataFrame({
#    'height':[150,155,160,165],
#    'weight':[50,55,60,65]
# })


# sns.jointplot(x='height',y='weight',kind='kde',data=df)

# plt.show()

# df=sns.load_dataset('tips')
# print (df)

# sns.boxplot(x='day',y='total_bill',data=df,)
# plt.show()

# task 5
# df=sns.load_dataset('titanic')
# print(df.head())

# sns.pairplot(data=df)
# plt.show()

# day 3 task 1
# df=sns.load_dataset('tips')
# print(df.head())

# sns.countplot(x='day',data=df)
# plt.show()

# tadk 2
# df=sns.load_dataset('tips')
# print(df.head())


# sns.barplot(x='day',y='total_bill',hue='sex',data=df,)
# plt.show()

# /task3
# sns.violinplot(x='time',y='total_bill',data=df,hue='sex')
# plt.show()
# # sns.stripplot(x='time',y='total_bill',data=df,hue='sex')
# # plt.show()

# tyask4
# sns.countplot(x='sex',data=df)
# plt.show()
# df=pd.DataFrame({
#     'subjects':['Eng','Mat','Sci']
#     ,'marks':[89,90,95]
# })

# sns.barplot(x='subjects',y='marks',data=df)
# plt.show()
# # task 5
# df=pd.DataFrame({
#     'age':[30,35,40,45,20,22],
#     'gender':['female','male','male','female','male','male']
# })
# sns.violinplot(x='gender',y='age',data=df,hue='gender')

# plt.show()
# task 6 
# df=pd.DataFrame({
#            'Department':['HR','Accounting','Marketing','Sales','Finance'],
#        'Years of Experience': [1,2,4,2,5]
# })

# sns.swarmplot(x='Department',y='Years of Experience',data=df)

# plt.show()

# day 4 task1 

# df=pd.DataFrame({
#            'Department':['HR','Accounting','Marketing','Sales','Finance'],
# 'Years of Experience': [1,2,4,2,5]
# })

# sns.swarmplot(x='Department',y='Years of Experience',data=df,hue='Department')

# plt.show()

# # task 1


# task2 
# df=pd.DataFrame({
#     'Math':[80,89,97,95],
#     'Science':[90,70,85,70],
#     'English':[90,98,95,89],
#     'IT': [98,95,98,100]

# },index=['Student1','Student2','Student3','Student4'])
# sns.clustermap(data=df,cmap='coolwarm',annot=True)
# plt.show()

# task 3
# data=np.random.randint(1,100,size=(5,5))

# sns.heatmap(data,annot=True,cmap='viridis')
# plt.show()

# # task 4
# df=pd.DataFrame({
#     'Age':[22,25,26,27,30],
#     'Salary':[30000,40000,350000,520000,60000],
#     'Expereinece':[1,3,4,2.5,1],
#     'Department':['HR','IT','Accoundant','Finanace','IT']
# })
# numeric_df=df.select_dtypes(include='number')

# corr=numeric_df.corr()

# sns.heatmap(corr,annot=True,cmap='coolwarm')
# plt.show()