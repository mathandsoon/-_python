#章末問題5.9
#AtCoder Educational DP Contest N Slimes

N=int(input())
a=list(map(int,input().split()))

Table=[[0]*(N+1) for _ in range(N+1)]
for i in range(N):
    for j in range(i+1,N+1):
        Table[i][j]=Table[i][j-1]+a[j-1]

dp=[[0]*(N+1) for _ in range(N+1)]

for loop in range(2,N+1):
    for i in range(N+1):
        for j in range(N+1):
            if j==i+loop:
                dp[i][j]=dp[i][i+1]+dp[i+1][j]+Table[i][j]
                for k in range(i+1,j):
                    dp[i][j]=min(dp[i][j],dp[i][k]+dp[k][j]+Table[i][j])


print(dp[0][N])