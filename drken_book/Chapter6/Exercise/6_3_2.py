#章末問題6.3
#第7回JOI 本選 問3 ダーツ
#https://atcoder.jp/contests/joi2008ho/tasks/joi2008ho_c

"""半分全列挙というアルゴリズムを用いる。"""
from bisect import bisect_right

N,M=map(int,input().split())
P=[]
for i in range(N):
    P.append(int(input()))

P.append(0)
S=[]
for i in range(N+1):
    for j in range(i,N+1):
        S.append(P[i]+P[j])

S.sort()
ans=0
for i in range(len(S)):
    if S[0]+S[i]>M:
        continue
    elif S[-1]+S[i]<=M: ans=max(ans,S[-1]+S[i])
    else:
        b=bisect_right(S,M-S[i])
        b=max(b-1,0)
        ans=max(ans,S[b]+S[i])

print(ans)