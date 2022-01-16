#章末問題6.4
#POJ No.2456 Agressive-Cows
#http://poj.org/problem?id=2456

"""
POJはPython非対応!
なので、同じアルゴリズムを書いたC++で正解することを
確認しました。
（愚痴:FortanよりPython入れろー－－－。）
"""

N,M=map(int,input().split())
a=list(map(int,input().split()))

"""
元の問題ではaがソートされていないので、
a.sort()
が必要
"""

left,right=0,a[-1]
while right-left>1:
    mid=(left+right)//2
    cur,cnt=a[0],1
    for i in range(1,N):
        if a[i]-cur>=M:
            cur=a[i]
            cnt+=1
    if cnt>=M: left=mid
    else: right=mid

print(left)