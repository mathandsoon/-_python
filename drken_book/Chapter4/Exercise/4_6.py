#章末問題4.6

N,W=map(int,input().split())
a=list(map(int,input().split()))

memo=[[-1]*(W+1) for _ in range(N+1)]

def func(i,w):
    if i==0:
        if w==0: return True
        else: return False

    if memo[i][w]!=-1:
        return memo[i][w]

    if func(i-1,w):
        memo[i][w]=True
        return True

    if W[i-1]<=w:
        if func(i-1,w-W[i-1]):
            memo[i][w]=True
            return True

print(memo[-1][-1])
    
"""
分からなければ、
次章の動的計画法を勉強してから戻ってくるとよい。
"""