#Frog問題に対する、再帰関数を用いる単純な全探索

#rec(i): 足場0から足場iまでいたるまでの最小コスト

def rec(i):
    if i==0: return 0

    #答えを格納する変数を INF に初期化する
    res=INF

    #頂点i-1から来た場合
    res=min(res,rec(i-1)+abs(h[i]-h[i-1]))

    #頂点i-2から来た場合
    if i>1: res=min(res,rec(i-2)+abs(h[i]-h[i-2]))

    #答えを返す
    return res