#章末問題5.4

N,W,k=map(int,input().split())
a=list(map(int,input().split()))

INF=1<<30
dp=[[INF]*(W+1) for _ in range(N+1)]
dp[0][0]=0

for i in range(N):
    for j in range(W+1):
        if j>=a[i]:
            dp[i+1][j]=min(dp[i][j],dp[i][j-a[i]]+1)
        else:
            dp[i+1][j]=dp[i][j]

if dp[-1][-1]<=k:
    print("Yes")
else: print("No")