#输入四轴坐标若干，返回三轴坐标（元组）
def hex2Cubic(*points):
    ret=[]
    for point in points:
        (u,v,t,w)=point
        U=u-t
        V=v-t
        W=w
        ret.append((U,V,W))
    return tuple(ret)

#输入三轴坐标若干，返回四轴坐标（元组）
def cubic2Hex(*points):
    ret=[]
    for point in points:
        (U,V,W)=point
        u=(2*U-V)/3
        v=(2*V-U)/3
        t=-(u+v)
        w=W
        ret.append((u,v,t,w))
    return tuple(ret)
