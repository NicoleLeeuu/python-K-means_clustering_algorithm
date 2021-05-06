import matplotlib
import numpy as np
import random
from matplotlib.pyplot import plot, scatter

colors=['b','c','g','k','m','r','y']
#因为最后需要不同颜色绘图，但python不是很精通，所以最后采取了手动变色（滑稽

def loadData(filename):  #把数据导入
    infile = open(filename, 'r')
    x = []
    y = []
    for line in infile:
        trainningset = line.split(' ', 1)
        x.append(trainningset[0])
        trainningset[1] = trainningset[1].replace('\n','')
        #这里也是因为我的python技术不精，不知道为啥划分后trainningset[1]后多了换行符，只好手动切除了
        y.append(trainningset[1])
    x = [np.double(item) for item in x]
    y = [np.double(item) for item in y]
    return x, y

def distance(a,b,c,d): #最简单的距离计算方法哈！
    return pow(pow((a-c),2)+pow((b-d),2), 0.5)

def iteration(k,meansx,meansy,x,y):
#kmeans的核心函数，找到最终的均值向量
    while 1:
        Cx = [[] for i in range(k)]
        Cy = [[] for i in range(k)]
        ans = []
        finalmeansx = []
        finalmeansy = []
        for item in range(len(x)):
            mindis = 1000
            minindex = -1
            for ele in range(k):
                if distance(x[item],y[item],meansx[ele],meansy[ele]) < mindis:
                    mindis = distance(x[item],y[item],meansx[ele],meansy[ele])
                    minindex = ele
            ans.append(minindex)
            Cx[minindex].append(x[item])
            Cy[minindex].append(y[item])
        for i in range(k):
            finalmeansx.append(np.mean(Cx[i]))
            finalmeansy.append(np.mean(Cy[i]))
        if finalmeansx == meansx and finalmeansy == meansy:
            break
        else:
            meansx = finalmeansx
            meansy = finalmeansy
    return finalmeansx,finalmeansy,Cx,Cy,ans

def kmeans(k,x,y):
    meansx = random.sample(x, k)
    meansy = random.sample(y, k)
    print(meansx)
    print(meansy)
    finalmeansx,finalmeansy,Cx,Cy,ans = iteration(k,meansx,meansy,x,y)
    #修改后代码：
    f = open("E:\query.txt",'a')
    for item in range(k):
        f.write("第"+item.__str__()+"个簇:\n")
        f.write("均值中心为（"+finalmeansx[item].__str__()+","+finalmeansy[item].__str__()+")\n")
        scatter(finalmeansx[item], finalmeansy[item],c=colors[item],marker='x')
        f.write("簇内元素有："+len(Cx[item]).__str__()+"个\n")
        for i in range(len(Cx[item])):
            f.write("("+Cx[item][i].__str__()+","+Cy[item][i].__str__()+")\n")
            scatter(Cx[item][i],Cy[item][i],c=colors[item])
    """
    #以下就是在输出框输出分类结果
    for item in range(k):
        print("第"+item.__str__()+"个簇:\n")
        print("均值中心为（"+finalmeansx[item].__str__()+","+finalmeansy[item].__str__()+")\n")
        #最终簇中心用x突显
        scatter(finalmeansx[item], finalmeansy[item],c=colors[item],marker='x')
        print("簇内元素有："+len(Cx[item]).__str__()+"个\n")
        for i in range(len(Cx[item])):
            print("("+Cx[item][i].__str__()+","+Cy[item][i].__str__()+")\n")
            #画散点图
            scatter(Cx[item][i],Cy[item][i],c=colors[item])"""



datax,datay = loadData("E:\data.txt")
k = int(input("请问需要分为几类："))
kmeans(k,datax,datay)
#刚开始不知道为什么不弹出画图框，后来加了这个就出来啦
matplotlib.pyplot.figure(1)
matplotlib.pyplot.show()