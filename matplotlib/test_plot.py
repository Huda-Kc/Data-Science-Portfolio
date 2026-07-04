
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# drawing simple line  basic plotting

# xpoints=np.array([0,6])
# ypoints=np.array([0,20])
# plt.plot(xpoints,ypoints)
# plt.show()

# x=np.array([1,2,3,4,5])
# y=np.array([2,4,6,8,10])
# plt.plot(x,y)
# plt.show()

# markers
# x=np.array([1,2,3,4,5])
# y=np.array([2,4,6,8,10])
# plt.plot(x,y,marker='*')
# plt.show()

# markers style:

# y=np.array([2,4,6,8,10,12])
# plt.plot(y)
# plt.show()

# matplotlib formating
# y=np.array([3,8,1,10])
# plt.plot(y,'*:r')
# plt.show()
# marker size
# y=np.array([3,8,1,10])
# plt.plot(y,marker='o',ms=5)
# plt.show()

# markers edge color
# y=np.array([3,8,1,10])
# plt.plot(y,marker='o',mec='g')
# plt.show()
# marker face color
# y=np.array([3,8,1,10])
# plt.plot(y,marker='o',mfc='g',mec='black',ms=10)
# plt.show()

# line style
# y=np.array([3,8,1,10])
# plt.plot(y,marker='D',mec='r',c='red')
# plt.show()

# part 2
# multiple lines plot cheyyan
# x1=np.array([0,1,2,3])
# y1=np.array([3,6,9,0])
# x2=np.array([0,1,2,3])
# y2=np.array([7,8,3,4])
# plt.plot(x1,y1,x2,y2)
# plt.show()

# x1=np.array([0,1,2,3])
# y1=np.array([3,6,9,0])
# x2=np.array([0,1,2,3])
# y2=np.array([7,8,3,4])
# plt.plot(x1,y1,x2,y2)
# plt.xlabel('x data')
# plt.ylabel('y data')
# plt.title('The Data',loc='left')
# plt.show()

# subplots
# x=np.array([1,2,3,4])
# y=np.array([0,8,1,9])
# plt.subplot(1,2,1)
# plt.plot(x,y)

# # plot 2
# x=np.array([1,2,3,4])
# y=np.array([0,8,1,9])
# plt.subplot(1,2,2)
# plt.plot(x,y)

# plt.show()

# 6plots in a subject
# plt1
# x=np.array([1,2,3,4])
# y=np.array([0,8,1,9])
# plt.subplot(2,3,1)
# plt.title('plot 1')
# plt.xlabel('x values')
# plt.ylabel('y values')
# plt.plot(x,y)

# # plt2
# x=np.array([1,2,3,4])
# y=np.array([0,8,1,9])
# plt.subplot(2,3,2)
# plt.title('plot 2')
# plt.xlabel('x values')
# plt.ylabel('y values')
# plt.plot(x,y)

# # plot 3
# x=np.array([1,2,3,4])
# y=np.array([0,8,1,9])
# plt.subplot(2,3,3)
# plt.title('plot 3')
# plt.xlabel('x values')
# plt.ylabel('y values')
# plt.plot(x,y)

# # plot 4
# x=np.array([1,2,3,4])
# y=np.array([0,8,1,9])
# plt.subplot(2,3,4)
# plt.title('plot 4')
# plt.xlabel('x values')
# plt.ylabel('y values')
# plt.plot(x,y)

# # plot5
# x=np.array([1,2,3,4])
# y=np.array([10,20,30,40])
# plt.subplot(2,3,5)
# plt.title('plot 5')
# plt.xlabel('x values')
# plt.ylabel('y values')
# plt.plot(x,y)

# # plot6
# x=np.array([3,4,5,6])
# y=np.array([10,20,30,40])
# plt.subplot(2,3,6)
# plt.title('plot 6')
# plt.xlabel('x values')
# plt.ylabel('y values')
# plt.plot(x,y)

# plt.show()

# part 3

# scatter plot()
# x=np.array([3,5,7,2,6,1,8,5,8,11])
# y=np.array([1,3,5,10,6,4,8,2,13,3])
# plt.scatter(x,y)
# plt.show()

# plot 1
# x=np.array([3,5,7,2,6,1,8,5,8,11])
# y=np.array([1,3,5,10,6,4,8,2,13,3])
# plt.scatter(x,y)

# # plot 2
# x1=np.array([11,14,17,18,14,19,10,20,11,21])
# y1=np.array([1,4,7,20,14,12,11,10,25,27])
# plt.scatter(x1,y1)
# plt.show()


# x1=np.array([11,14,17,18,14,19,10,20,11,21])
# y1=np.array([1,4,7,20,14,12,11,10,25,27])
# plt.scatter(x1,y1,color='black')
# plt.show()

# difernt colors of each dot
# x1=np.array([11,14,17,18,14,19,10,20,11,21])
# y1=np.array([1,4,7,20,14,12,11,10,25,27])
# colors=np.array(['red','blue','black','purple','grey','yellow','orange','green','pink','lavender'])
# plt.scatter(x1,y1,c=colors)

# plt.show()

# x1=np.array([11,14,17,18,14,19,10,20,11,21])
# y1=np.array([1,4,7,20,14,12,11,10,25,27])
# size=np.array([50,60,100,10,250,25,45,75,90,30])
# plt.scatter(x1,y1,s=size)
# plt.show()

# alpha transperncy   0 to 1
# x1=np.array([11,14,17,18,14,19,10,20,11,21])
# y1=np.array([1,4,7,20,14,12,11,10,25,27])
# size=np.array([50,60,100,10,250,25,45,75,90,30])
# plt.scatter(x1,y1,s=size,alpha=1)
# plt.show()

# color map
# x=np.array([1,9,12,10,17,4,6,9,16,20])
# y=np.array([10,11,15,18,13,3,7,0,3,23])
# plt.scatter(x,y,cmap='tab20b')
# plt.colorbar()
# plt.show()

# bar chart 
# x=np.array(['A','B','C','D'])
# y=np.array([10,20,30,40])
# plt.bar(x,y)
# plt.show()

# x=np.array(['A','B','C','D'])
# y=np.array([10,20,30,40])
# # horizntal
# plt.barh(x,y)
# plt.show()

# change color
# x=np.array(['A','B','C','D'])
# y=np.array([10,20,30,40])
# plt.bar(x,y,color='green')
# plt.show()
# bar chart size
# x=np.array(['A','B','C','D'])
# y=np.array([10,20,30,40])
# plt.bar(x,y,width=0.5)
# plt.show()

# pie chart
# y=np.array([35,25,25,15])
# plt.pie(y)
# plt.show()

# create labels
# y=np.array([35,25,25,15])
# mylabels=['class 1','class 2','class 3', 'class 4']
# plt.pie(y,labels=mylabels)
# plt.show()

# exploaded function
# y=np.array([35,25,25,15])
# mylabels=['class 1','class 2','class 3', 'class 4']
# mycolor=['yellow','black','pink','grey']
# myexplode=[0.1,0.3,0,0.1]
# plt.pie(y,labels=mylabels,colors=mycolor,explode=myexplode,shadow=True)
# plt.show()

# legends
# y=np.array([35,25,25,15])
# mylabels=['class 1','class 2','class 3', 'class 4']
# plt.pie(y,labels=mylabels)
# plt.legend()
# plt.show()

# part 4
# Seaborn
