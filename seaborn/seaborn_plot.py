import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns 

# part 4
# print(sns.get_dataset_names())

# df=sns.load_dataset('car_crashes')
# print(df)
# df.shape
# print(df)

# plt.scatter(df.speeding,df.alcohol)
# plt.show()

# data_set=sns.load_dataset('iris')
# print(data_set)

# sns.lineplot(x='sepal_length',y='sepal_width',data=data_set)
# plt.title('flower data set')
# plt.show()

# part 5
# categorical plots
# bar plot
# dataset=sns.load_dataset('iris')
# print(dataset)

# sns.barplot(x='species',y='sepal_width',data=dataset)
# plt.show()

# pallete
# sns.barplot(x='species',y='sepal_width',palette='pastel',data=dataset)
# plt.show()

# countplot
# data=sns.load_dataset('iris')
# print(data)
# sns.countplot(x='species',palette='bright',data=data)
# plt.show()

# box plot
# sns.boxplot(x='species',y='sepal_length',data=data)
# plt.show()

# violin plot
# sns.violinplot(x='species',y='sepal_width',data=data)
# plt.show()

# distribution plot
# 1) histogram
# sns.histplot(x='species',data=data)
# plt.show()

# displot 
# tips=sns.load_dataset('tips')
# print(tips)
# sns.displot(tips['total_bill'],kde=True)
# plt.show()

# pairplot
# data=sns.load_dataset('iris')
# print(data)
# sns.pairplot(data=data,hue='species')
# plt.show()

# heatmap
# tips=sns.load_dataset('tips')
# print(tips)
# tc=tips.corr(numeric_only=True)
# sns.heatmap(tc,cmap='plasma')
# plt.show()

# tips=sns.load_dataset('tips')
# print(tips)
# tc=tips.corr(numeric_only=True)
# sns.heatmap(tc,annot=True,cmap='plasma',linecolor='black')
# plt.show()

df=sns.load_dataset('tips')

corr=df.corr(numeric_only=True)

sns.heatmap(corr,cmap='coolwarm',annot=True)
# x=[0,1,2,3]
# y=[1,2,3,4]
# plt.plot(x,y)
# x1=np.array([1,2,3,4])
# y1=np.array([5,6,7,8])
# plt.xlabel('x-axis')
# plt.ylabel('y-axis')
# plt.title('Chart')
# plt.plot(x1,y1, '-.')
# plt.fill_between(x,y,y1,color='green',alpha=0.5)
# plt.show()


# barchart
# fruits=['Apple','Bnana','Cherry']
# sales=[300,350,400]

# plt.bar(fruits,sales,color='violet',width=0.5)
# plt.title('fruit sales')
# plt.xlabel('fruits')
# plt.ylabel('sales')
# plt.show()

# scatterplot
# x=np.array([160,164,167,169,170,174,175,179,180,183])
# y=np.array([51,53,55,57,59,60,63,67,69,70])

# a=[20,50,100,200,500,1000,60,90,150,300]
# b=['red','green','blue','purple','orange','black','pink','brown','yellow','cyan']
# plt.scatter(x,y,s=a,c=b,alpha=0.6,edgecolors='w',linewidths=1)
# plt.title("Scatter Plot with Varying Colors and Sizes")


# plt.show()

# x=np.random.randint(50,150,100)
# y=np.random.randint(50,150,100)
# colors= np.random.rand(100)
# sizes=20*np.random.randint(10,100,100)

# plt.scatter(x,y,marker='^',color='magenta',s=100,alpha=0.7)
# plt.colorbar(label='color scale')
# plt.title("Scatter Plot with Colormap and Colorbar")
# plt.show()

# histogram
# data=np.random.randn(1000)
# sns.histplot(data,bins=30,kde=True, color='lightgreen',edgecolor='red')

# plt.xlabel('values')
# plt.ylabel('density')
# plt.title("Scatter Plot with Colormap and Colorbar")

# plt.show()

# data1=np.random.randn(1000)
# data2=np.random.normal(loc=3, scale=1, size=1000)

# fig,axes=plt.subplots(nrows=1,ncols=2,figsize=(12,4))

# axes[0].hist(data1, bins=30, color='yellow',edgecolor='black')
# axes[0].set_title('hist 1')

# axes[1].hist(data2,bins=30, color='pink',edgecolor='black')
# axes[1].set_title('hist 2')

# for ax in axes:
#     ax.set_xlabel('values')
#     ax.set_ylabel('frequency')

#     plt.tight_layout()

#     plt.show()

# pie chart
# cars=['AUDI','BMW','FORD','TESLA','JAGUAR']
# data=[23,17,35,29,12]

# explode=(0.1,0.0,0.2,0.3,0.0,0.0)

# colors=('orange','cyan','brown','grey','indigo')

# wp={'linewidth': 1, 'edgecolor' : 'green'}

# fig=plt.figure(figsize=(10,7))
# plt.pie(data,labels=cars)

# plt.show()

# df=sns.load_dataset('tips')

# df.head()
# print(df)

# sns.set_style('whitegrid')
# sns.jointplot(x ='total_bill', y ='tip', data = df,kind='kde')
# plt.show()

# df=sns.load_dataset('tips')
# df.head(7)
# print(df)
# sns.set_style('darkgrid')
# sns.catplot(x='day',y='total_bill', data=df,kind='bar')
# plt.show()

# heat map
# data=np.random.randint(1,100,(10,10))

# sns.heatmap(data, cmap='coolwarm',center=50)
# plt.show()

# clust map
# data=sns.load_dataset('flights')

# frequency_encoding(data,'month')
# sns.clustermap(data, figsize=(7,7))
# plt.show()




# trial line chart
# x=[1,2,3,4]
# y=[1,3,2,5]

# plt.plot(x,y)
# plt.xlabel("X-axis")
# plt.ylabel('y-axis')
# plt.title("simple line plot")
# plt.show()


# x=[1,2,3,4]
# y=[1,3,2,5]

# plt.plot(x,y)
# plt.plot(x,[2,4,6,8])
# plt.legend(['line 1','line 2'])
# plt.show()

# bar chart
# students= ['A','B','c']
# marks=[85,90,78]

# plt.bar(students,marks)
# plt.xlabel('Students')
# plt.ylabel('Marks')
# plt.title('Student Marks')
# plt.show()

# histogram
# data=np.random.randn(100)
# plt.hist(data, bins=10)
# plt.title('histogram')
# plt.show()

# scatter plot
# age=[10,12,14,16]
# height=[140,150,160,170]

# plt.scatter(age,height)
# plt.xlabel('Age')
# plt.ylabel('Height')
# plt.show()

# subplots
# plt.subplot(1,2,1)
# plt.plot([1,2,3],[4,5,6])

# plt.subplot(1,2,2)
# plt.plot([1,2,3],[3,2,5])

# plt.show()


# x=[1,2,3,4]
# y=[1,3,2,5]

# plt.plot(x,y,color='red',marker='o',linestyle='--')
# plt.title('sample ')
# plt.show()


# sns.barplot(x='day',y='total_bill',data=df)
# plt.show()

# sns.countplot(x='sex',data=df)
# plt.show()

# sns.boxplot(x='day',y='total_bill',data=df)
# plt.show()

# sns.violinplot(x='sex',y='total_bill',data=df)
# plt.show()


# df=sns.load_dataset('tips')
# print(df)

# plt.bar(df['day'],df['total_bill'])
# plt.show()

# plt.subplot(1,2,1)
# sns.boxplot(x='sex',y='total_bill',data=df)

# plt.subplot(1,2,2)
# sns.violinplot(x='sex',y='total_bill',data=df)

# plt.show()