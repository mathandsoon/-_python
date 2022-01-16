#章末問題5.1
#AtCoder Educational DP Contest C Vacation

N=int(input())
Vacation=[]
for i in range(N):
    Vacation.append(list(map(int,input().split())))

dp=[[0,0,0] for _ in range(N+1)]
for i in range(N):
    dp[i+1][0]=max(dp[i][1]+Vacation[i][0],dp[i][2]+Vacation[i][0])
    dp[i+1][1]=max(dp[i][0]+Vacation[i][1],dp[i][2]+Vacation[i][1])
    dp[i+1][2]=max(dp[i][0]+Vacation[i][2],dp[i][1]+Vacation[i][2])

print(max(dp[-1]))