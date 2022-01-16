#ナップサック問題に対する動的計画法

#入力
N,W=map(int,input().split())
weight,value=[],[]
for i in range(N):
    w,v=map(int,input().split())
    weight.append(w)
    value.append(v)

#DP テーブル定義
dp=[[0]*(W+1) for _ in range(N+1)]

# DPループ
for i in range(N):
    for w in range(W+1):
        if w-weight[i]>=0:
            #i番目の品物を選ぶ場合
            dp[i+1][w]=max(dp[i+1][w],dp[i][w-weight[i]]+value[i])

        #i番目の品物を選ばない場合
        dp[i+1][w]=max(dp[i+1][w],dp[i][w])

print(dp[-1][-1])

"""
AtCoder Educational DP Contest D Knapsack1
にナップサック問題があるが、
Python3だと遅くてTLEになるので、
言語をPyPy3にして実行するとよい。
(PyPy3はPythonの処理の一部をC言語で行うことで、
Pythonの処理を高速化させた言語)
"""