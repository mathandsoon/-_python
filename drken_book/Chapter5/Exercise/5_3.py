#章末問題5.3
#AtCoder Typical DP Contest A コンテスト

N=int(input())
P=list(map(int,input().split()))

dp=[[False]*(sum(P)+1) for _ in range(N+1)]
dp[0][0]=True
for i in range(N):
    for j in range(sum(P)+1):
        if j>=P[i]:
            dp[i+1][j]=dp[i][j] or dp[i][j-P[i]]
        else:
            dp[i+1][j]=dp[i][j]

print(sum(dp[-1]))

"""
bool型の整数型への変換は、
True->1
False->0
である。
余談だが、コンピュータの内部ではbool型とint型の
管理は本質的な意味で同じ方法がとられている。
"""