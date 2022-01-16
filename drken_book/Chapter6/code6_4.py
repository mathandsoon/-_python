#二分探索法を用いて、「ペア和を最適化する問題」に対する全探索解法を高速化する

"""std:lower_boundの対応物"""
def lower_bound(key,a):
    left,right=0,len(a)-1
    if a[right]<key: return len(a)
    while right-left>1:
        mid=(left+right)//2
        if a[mid]<key: left=mid
        else: right=mid
    return right

INF=2*10**7 #十分大きな値に 

#入力を受け取る
N,K=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))

#暫定最小値を格納する変数
min_value=INF

#bをソート
b.sort()

#bに無限大を表す数値(INF)を追加しておく
#これを行うことで、
# 配列内にkeyを満たすiが存在しない場合をなくせる。
# (なくてもやってることは変わらないが、C++だと恩恵を受けれた。)
b.append(INF)

#aを固定しておく
for i in range(N):
    val=lower_bound(b,K-a[i])

    #min_valueと比較する
    if a[i]+val<min_value:
        min_value=a[i]+val

print(min_value)