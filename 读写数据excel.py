# -*- coding: utf-8 -*-
"""
Created on Tue Jul 18 14:48:51 2017

@author: Lenovo-Y430p
"""
#读写数据excel
#通过try把空格变成nan
import xlrd
import xlwt
from numpy import nan
def loaddata():
    dataMat = []; labelMat = []
    data = xlrd.open_workbook(r'C:\Users\Lenovo-Y430p\Desktop\数据\分类数据.xlsx')
    table = data.sheets()[0]
    nrows = table.nrows #行数
    ncols = table.ncols #列数
    for i in range(0,nrows):
        temp=[]
        rowValues= table.row_values(i) #某一行数据 
        for j in range(ncols-1):
            try:
                temp.append(float(rowValues[j]))
            except:
                temp.append(nan)
        dataMat.append(temp)
        labelMat.append(float(rowValues[-1]))
    print(dataMat,labelMat)
    return dataMat,labelMat

def WriteSheetRow(sheet,rowValueList,rowIndex,isBold):
    i = 0
    #style = xlwt.easyxf('font: bold 1')
    style = xlwt.easyxf('font: bold 0, color red;')#红色字体
    #style2 = xlwt.easyxf('pattern: pattern solid, fore_colour yellow; font: bold on;') # 设置Excel单元格的背景色为黄色，字体为粗体
    for svalue in rowValueList:
        strValue = str(svalue)
        if isBold:
            sheet.write(rowIndex,i,strValue,style)
        else:
            sheet.write(rowIndex,i,strValue)
        i = i + 1
'''写excel文件''' 
def save_Excel():
    wbk = xlwt.Workbook(encoding='utf8')
    sheet = wbk.add_sheet('sheet2',cell_overwrite_ok=True)
    headList = ['age','age','age','ni']
    rowIndex = 0
    WriteSheetRow(sheet,headList,rowIndex,True)
    for i in range(1,5500):
        rowIndex = rowIndex + 1
        valueList = []
        for j in range(1,5):
            valueList.append(j*i)
        WriteSheetRow(sheet,valueList,rowIndex,False)
    wbk.save('Excel_Workbook.xls')
loaddata()