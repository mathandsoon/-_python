#章末問題5.6

N,W=map(int,input().split())
a=list(map(int,input().split()))
m=list(map(int,input().split()))

INF=1<<60
dp=[[INF]*(W+1) for _ in range(N)]
dp[0][0]=0

for i in range(N):
    for j in range(W+1):
        if dp[i][j]<INF:
            dp[i+1][j]=0
        else:
            if j>=a[i] and dp[i+1][j-a[i]]<m[i]:
                dp[i+1][j]=min(dp[i+1][j],dp[i+1][j]+1)

if dp[-1][-1]<=m[-1]:
    print("Yes")
else: print("No")