#章末問題5.2

N,W=map(int,input().split())
a=list(map(int,input().split()))

dp=[[False for _ in range(W+1)] for _ in range(N+1)]
dp[0][0]=True
for i in range(N):
    for j in range(W+1):
        if a[i]>j:
            dp[i+1][j]=dp[i][j]
        else:
            dp[i+1][j]=dp[i][j] or dp[i][j-a[i]]