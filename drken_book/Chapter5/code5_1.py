#Frog問題を動的計画法で解く
#AtCoder Educational DP Contest A Frog1

#十分大きな値とする（ここでは2^60）
INF=1<<60

N=int(input())
h=list(map(int,input().split()))

#配列dpを定義（配列全体を無限大を表す値に初期化）
dp=[INF for _ in range(N)]

#初期条件
dp[0]=0

#ループ
for i in range(1,N):
    if i==1:
        dp[i]=abs(h[i]-h[i-1])
    else:
        dp[i]=min(dp[i-1]+abs(h[i]-h[i-1]),dp[i-2]+abs(h[i]-h[i-2]))

#答え
print(dp[-1])