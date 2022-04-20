#导入numpy库
#import numpy as np
#import matplotlib.pyplot as plt
from imports.FileHandleVESTA import fileHandlew
from imports.FileHandleVESTA import outputData
from imports.Factors import *

files=("C:\\Users\\Jacky Z\\Desktop\\fAl.txt",
       "C:\\Users\\Jacky Z\\Desktop\\FAl2.txt")

fileHandlew(files)

#以矩阵形式读入所有数据
dataAl,dataAlf=getMatrixDatas(files[0],files[1])

#plt.plot(dataAl[:,7],dataAl[:,6])
#plt.xlabel("2theta")
#plt.ylabel("f")
#plt.show()

h,k,l,f,F=getDatas(dataAl,dataAlf)

Ft=getF_mod(f,h,k,l,(0,0,0),(0,0.5,0.5),(0.5,0,0.5),(0.5,0.5,0))

err=getError(F,Ft)
#print(err)
#print("max:"+str(max(err)))
outputData("C:\\Users\\Jacky Z\\Desktop\\output.txt",h,k,l,f,F,Ft,err)
#print(output.shape)
