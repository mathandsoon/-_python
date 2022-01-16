#区間ごとに分割する方法を最適化する

INF=1<<60 #十分大きな値（ここでは2^60）

#入力
N=int(input())
c=[]
for i in range(N+1):
    c.append(list(map(int,input().split())))

#DPテーブル定義
dp=[INF for _ in range(N+1)]

#DP初期条件
dp[0]=0

#DPループ
for i in range(N+1):
    for j in range(i):
        dp[i]=min(dp[i],dp[j]+c[j][i])

#答えの出力
print(dp[N])