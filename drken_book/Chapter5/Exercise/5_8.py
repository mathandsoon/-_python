#章末問題5.8
#立命館プログラミングコンテスト 2018 day1 D
#https://onlinejudge.u-aizu.ac.jp/problems/2877

N,M=map(int,input().split())
a=list(map(int,input().split()))

Table=[[0]*(N+1) for _ in range(N+1)]
for i in range(N):
    for j in range(i+1,N+1):
        Table[i][j]=Table[i][j-1]+a[j-1]

for i in range(N):
    for j in range(i+1,N+1):
        Table[i][j]/=j-i

dp=[[0]*(N+1) for _ in range(M)]
for i in range(N+1):
    dp[0][i]=Table[0][i]

for i in range(M-1):
    for j in range(N+1):
        for k in range(j):
            dp[i+1][j]=max(dp[i+1][j],dp[i][k]+Table[k][j])

print(dp[-1][-1])

"""
Pythonだと遅くて、上のAOJだとTLEになります。
"""