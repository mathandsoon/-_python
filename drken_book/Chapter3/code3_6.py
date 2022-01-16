#部分和問題に対するビットを用いる全探索解法

#入力受け取り
N,W=map(int,input().split())
a=list(map(int,input().split()))

#bitは2^N通りの部分集合全体を動きます
exist=False
for bit in range(1<<N):
    Sum=0
    """
    元のコードでは変数名はsumになっているが、
    Pythonには組み込み関数のsumがあるので好ましくない。
    （ただし関数名は予約語ではないので変数にすることは一応できる。）
    """
    for i in range(N):
        #i番目の要素が含まれるの要素a[i]が部分集合に含まれているかどうか
        if bit & (1<<i):
            Sum+=a[i]
    if Sum==W:
        exist=True

if exist:
    print("Yes")
else:
    print("No")