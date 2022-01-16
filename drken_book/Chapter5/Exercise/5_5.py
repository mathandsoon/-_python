#章末問題5.5

N,W=map(int,input().split())
a=list(map(int,input().split()))

dp=[[0]*(W+1) for _ in range(N)]
dp[0][0]=1
for i in range(N):
    for j in range(W+1):
        dp[i+1][j]|=dp[i][j]
        if j>=a[i]:
            dp[i+1][j]|=dp[i+1][j-a[i]]

if dp[-1][-1]:
    print("Yes")
else: print("No")