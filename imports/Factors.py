import numpy as np

#计算结构因子
#实部
def getF_R(f,h,k,l,*points):
    FRhkl=0
    for p in points:
        FRhkl=FRhkl+f*np.cos(2*np.pi*(h*p[0]+k*p[1]+l*p[2]))

    return FRhkl

#虚部
def getF_I(f,h,k,l,*points):
    FIhkl=0
    for p in points:
        FIhkl=FIhkl+f*np.sin(2*np.pi*(h*p[0]+k*p[1]+l*p[2]))

    return FIhkl

#模
#对于单一原子可以直接计算结构因子的模
def getF_mod(f,h,k,l,*points):
    FRhkl=getF_R(f,h,k,l,*points)
    FIhkl=getF_I(f,h,k,l,*points)
    return np.sqrt(FRhkl**2+FIhkl**2)

#对于多原子
def getF_mods(FRhkl,FIhkl):
    return np.sqrt(FRhkl**2+FIhkl**2)



#给定若干文件，返回每一个文件的矩阵形式信息（tuple）
def getMatrixDatas(*files):
    ret = []
    for f in files:
        ret.append(np.genfromtxt(f,delimiter=' ',skip_header=True))
    return tuple(ret)

#给定原子散射因子文件（简单立方结构）与VESTA结构因子文件，输出(h,k,l,f,F)
#h、k、l为晶面，f为原子散射因子，F为VESTA得到的结构因子
def get_hkl(data):
    ret=[]
    ret.append(data[:,0])
    ret.append(data[:,1])
    ret.append(data[:,2])
    return ret

def get_f(data):
    return data[:,6]

    

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
