#章末問題6.1

a=list(map(int,input().split()))

"""配列aの座標圧縮を行う関数"""
def compress(a):
    b=sorted(a)
    res=[]
    for i in a:
        left,right=0,len(a)-1
        if b[left]==i:
            res.append(left)
            continue
        while right-left>1:
            mid=(left+right)//2
            if b[mid]<i: left=mid
            else: right=mid
        res.append(right)
    return res