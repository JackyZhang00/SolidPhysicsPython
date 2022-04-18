#导入numpy库
import numpy as np
import matplotlib.pyplot as plt
def fileHandle(file_in,file_out):
    for f1 in file_in:
        #打开原始文件
        f=open(f1,"r")
        #将数据以整行读入并做初始化
        a=f.readlines() #字符串序列
        r=[]
        #删除空格
        for s in a:
            r.append(" ".join(s.split())+"\n")
        #关闭文件
        f.close()
        #打开修改后的文件并导入数据
        f=open(file_out[file_in.index(f1)],"w")
        f.write("".join(r))
        f.close()
def getF(f,h,k,l,*points):
    Fhkl=0
    for p in points:
        Fhkl=Fhkl+f*np.cos(2*np.pi*(h*p[0]+k*p[1]+l*p[2]))

    return Fhkl



files=("C:\\Users\\Jacky Z\\Desktop\\fAl.txt",
       "C:\\Users\\Jacky Z\\Desktop\\FAl2.txt")
files2=("C:\\Users\\Jacky Z\\Desktop\\fAla.txt",
       "C:\\Users\\Jacky Z\\Desktop\\FAl2a.txt")
fileHandle(files,files2)
#以矩阵形式读入所有数据
dataAl = np.genfromtxt\
(files2[0], delimiter=' ',skip_header=True)
dataAlf = np.genfromtxt\
(files2[1], delimiter=' ',skip_header=True)
#plt.plot(dataAl[:,7],dataAl[:,6])
#plt.xlabel("2theta")
#plt.ylabel("f")
#plt.show()

f=dataAl[:,6]
F=dataAlf[:,6]
h=dataAl[:,0]
k=dataAl[:,1]
l=dataAl[:,2]

#Ft=f*(1+np.cos(2*np.pi*((h+k)/2))+np.cos(2*np.pi*((h+l)/2))
#     +np.cos(2*np.pi*((k+l)/2)))
Ft=getF(f,h,k,l,(0,0,0),(0,0.5,0.5),(0.5,0,0.5),(0.5,0.5,0))
err=np.abs(Ft-F)/(F+1e-6)
output=np.array([h,k,l,f,F,Ft,err])
#print(err)
#print("max:"+str(max(err)))
np.savetxt("C:\\Users\\Jacky Z\\Desktop\\output.txt",output.T,fmt="%8.6f")
#print(output.shape)
