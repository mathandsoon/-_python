#編集距離を動的計画法を用いて求める

INF=1<<29 #十分大きな値（ここでは2^29）

#入力
S,T=input().split()

#DPテーブル定義
dp=[[INF]*(len(T)+1) for _ in range(len(S)+1)]

#DP初期条件
dp[0][0]=0

#DPループ
for i in range(len(S)+1):
    for j in range(len(T)+1):
        #変更操作
        if i>0 and j>0:
            if S[i]==T[j]:
                dp[i][j]=min(dp[i][j],dp[i-1][j-1])
            else:
                dp[i][j]=min(dp[i][j],dp[i-1][j-1]+1)
        
        #削除操作
        if i>0: dp[i][j]=min(dp[i][j],dp[i-1][j]+1)

        #挿入操作
        if j>0: dp[i][j]=min(dp[i][j],dp[i][j-1]+1)

#答えの出力
print(dp[-1][-1])

"""
余談
編集距離の概念は復号に関する理論へも応用されます。
例えば、信号を送信するときに伝搬で情報が誤ったものに
なったとしても、情報を冗長にすれば元の情報を復元できます。
このとき、どのくらい情報を冗長にすればいいかについて
編集距離が定量的な解析方法を与えます。
"""