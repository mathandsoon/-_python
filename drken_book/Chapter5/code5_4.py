#Frog問題を「配る遷移形式」で解く

#十分大きな値とする（ここでは2^60）
INF=1<<60

N=int(input())
h=list(map(int,input().split()))

#初期化（最小化問題なのでINFで初期化）
dp=[INF]*N

#初期条件
dp[0]=0

#ループ
for i in range(N):
    if i+1<N:
        dp[i+1]=min(dp[i+1],dp[i]+abs(h[i]-h[i+1]))
    if i+2<N:
        dp[i+2]=min(dp[i+2],dp[i]+abs(h[i+2]-h[i]))

#答え
print(dp[-1])