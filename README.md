# SolidPhysicsPython
晶体可视化软件VESTA在固体物理学习中的应用 Python程序

作者：Jacky Zhang（Shandong University of Science and Technology）
## 关于本软件
本软件主要实现以下功能：
##### 根据VESTA软件计算结构因子

目前所实现的功能：
##### 根据晶胞的原子坐标计算单元素晶体的结构因子

## 更新记录
### v0.1
根据VESTA软件计算结构因子，计算单一元素晶体的结构因子并输出误差

### v0.2
设计若干库，其中包括
#### FileHandleVESTA
用于处理VESTA得到的文件
#### Factors
用于计算结构因子

### v0.3
支持多原子结构因子计算

关于所有库的使用可以查看相关代码

### v0.4
支持三轴坐标系与四轴坐标系坐标的相互转换

## 你需要安装的库
### numpy

### 如何安装这些库？
你可以使用pip指令，例如，使用pip install numpy可以用来安装numpy库

关于pip的相关操作，可以查找相关教程

## 一些常见的问题：
在使用的过程中，如果你遇到问题，可以先在这里看一下有没有你想要的。
### 文件名怎么输入？
对于Python而言，由于\表示转义字符，因此如果你需要输入文件当中的\，请使用两个反斜杠！

### 对于单原子和多原子的结构因子，要怎么计算？
对于单原子，目前可以直接调用getF_mod函数计算，需要传入的参数包括：散射因子f、晶面坐标、原子坐标

对于多原子，需要首先调用getF_R()和getF_I()得到多原子晶体的结构因子的实部和虚部，然后通过getF_mods()函数直接计算它的模。在调用getF_mods()的时候只需要传入getF_R()和getF_I()得到的数据即可。

### 我发现这个程序有问题，如何提出bug？
如果你遇到bug，欢迎提出来（建议也可以），使用issue是一个好方法！

当然，如果你有新的想法，也可以直接改进这些程序。这些程序都是开源的，你只要遵循相关协议即可。你也可以在GitHub上提出PR
