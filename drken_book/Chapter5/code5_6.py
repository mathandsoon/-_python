#Frog問題を「メモ化再帰」で解く

#十分大きな値とする（ここでは2^60）
INF=1<<60

#入力データと、メモ用のdpテーブル
N=int(input())
h=list(map(int,input().split()))
dp=[INF]*N

def rec(i):
    #DPの値が更新されていたらそのままリターン
    if dp[i]<INF:
        return dp[i]

    #ベースケース：足場0のコストは0
    if i==0:
        return 0

    #答えを表す変数をINFで初期化する
    res=INF

    #足場i-1から来た場合
    res=min(res,rec(i-1)+abs(h[i]-h[i-1]))

    #足場i-2から来た場合
    if i>1:
        res=min(res,rec(i-2)+abs(h[i]-h[i-2]))

    #結果をメモ化しながら返す
    dp[i]=res
    return dp[i]

"""
元のC++のコード内のmain関数内の
入力受け取りと初期化は事前に行ったので省略
"""    

print(rec(N-1))