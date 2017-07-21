# -*- coding: utf-8 -*-
"""
Created on Tue Jul 18 12:37:44 2017

@author: Lenovo-Y430p
"""
#读取txt文件
def loadDataSet(fileName):
    dataMat = []; labelMat = []
    try :
        fr = open(fileName)
    except IOError:
        print('could not open files') 
    for line in fr.readlines():
        temp=[]
        lineArr = line.strip().split('\t')
        for i in range(len(lineArr)-1):
            temp.append(float(lineArr[i]))
        dataMat.append(temp)
        labelMat.append(float(lineArr[-1]))
    print(dataMat,labelMat)
    fr.close()
    return dataMat,labelMat
#写入txt文件
def write(fileName):
    try :
        fr = open(fileName,'a+')
    except IOError:
        print('could not open files')
    fr.write('内容')
    f.write("\t")   
    f.write('内容2')
    f.write("\n")
    fr.writelines('list')#不会添加换行符
    fr.close()
loadDataSet(r'C:\Users\Lenovo-Y430p\Desktop\数据\分类数据.xlsx')

 