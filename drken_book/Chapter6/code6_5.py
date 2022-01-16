#射撃王問題に対する二分探索法
#AtCoder Beginner Contest 023 D 射撃王

INF=1<<60 #十分大きな値を1つ決める

#入力
N=int(input())
h,s=[0]*N,[0]*N
for i in range(N):
    h[i],s[i]=map(int,input().split())

#二分探索
left,right=0,INF
while right-left>1:
    mid=(left+right)//2

    #判定
    ok=True
    t=[0]*N #各風船を割るまでの時間制限
    for i in range(N):
        #そもそも高度がmidより低かったらFalse
        if mid<h[i]: ok=False
        else: t[i]=(mid-h[i])//s[i]

    #時間制限が差し迫っている順にソート
    t.sort()
    for i in range(N):
        if t[i]<i: ok=False #時間切れ発生

    if ok: right=mid
    else: left=mid

print(right)