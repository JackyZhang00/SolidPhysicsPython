import numpy as np

#计算结构因子
def getF(f,h,k,l,*points):
    Fhkl=0
    for p in points:
        Fhkl=Fhkl+f*np.cos(2*np.pi*(h*p[0]+k*p[1]+l*p[2]))

    return Fhkl

#给定若干文件，返回每一个文件的矩阵形式信息（tuple）
def getMatrixDatas(*files):
    ret = []
    for f in files:
        ret.append(np.genfromtxt(f,delimiter=' ',skip_header=True))
    return tuple(ret)

#给定原子散射因子文件（简单立方结构）与VESTA结构因子文件，输出(h,k,l,f,F)
#h、k、l为晶面，f为原子散射因子，F为VESTA得到的结构因子
def getDatas(dataf,dataF):
    ret=[]
    ret.append(dataf[:,0])
    ret.append(dataf[:,1])
    ret.append(dataf[:,2])
    ret.append(dataf[:,6])
    ret.append(dataF[:,6])
    return ret

#计算误差
def getError(F,Ft):
    return np.abs(Ft-F)/(F+1e-6)
