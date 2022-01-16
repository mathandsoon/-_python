#ペア和の最小値を求める（K以上の範囲）

INF=20000000 #十分大きな値に

#入力を受け取る
N,K=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))

#線形探索
min_value=INF
for i in range(N):
    for j in range(N):
        #和がK未満の場合は捨てる
        if a[i]+b[j]<K: continue
        #最小値を更新
        if a[i]+b[j]<min_value:
            min_value=a[i]+b[j]

#結果出力
print(min_value)