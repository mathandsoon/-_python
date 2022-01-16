#章末問題6.5
#AtCoder Regular Contest 037 C 億マス計算
#https://atcoder.jp/contests/arc037/tasks/arc037_c

N,K=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))

a.sort()
b.sort()
C=a[-1]*b[-1]

"""x以下の数がK個以上あるかどうかを判定する関数"""
def isin(x):
    ans=0
    for i in range(len(a)):
        if a[i]>x:
            break
        search=x//a[i]
        if b[0]>search:
            continue
        left,right=0,len(a)-1
        if b[-1]<=search:
            ans+=right+1
        else:
            while right-left>1:
                mid=(left+right)//2
                if b[mid]<=search: left=mid
                else: right=mid
            ans+=left+1
    if ans>=K: return True
    else: return False

left,right=0,C
while right-left>1:
    mid=(left+right)//2
    if isin(mid): right=mid
    else: left=mid
if K==1:
    print(a[0]*b[0])
else: print(right)