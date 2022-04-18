import numpy as np

#处理数据：从file_in当中删除空格并将其写入file_out当中
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

#处理数据：从file当中删除空格并写入file当中（覆盖）
def fileHandlew(files):
    fileHandle(files,files)

#输出数据：将data输出至file
def outputData(file,*data):
    output=np.array(data)
    np.savetxt(file,output.T,fmt="%8.6f")
