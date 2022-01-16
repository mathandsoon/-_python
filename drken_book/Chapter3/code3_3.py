#最小値を求める

INF=20000000 #十分大きな値に

"""無限大を表す方法として、十分大きな数を用意する以外にも、
Pythonの標準ライブラリにあるmathモジュールを使えば、
import math
INF=math.inf
として、便宜的に無限大を表す変数を用意できる。
ただし、通常の数と振る舞いが異なるので
適宜公式ドキュメント等を要参照。"""

#入力を受け取る
N=int(input())
a=list(map(int,input().split()))

#線形探索
min_value=INF
for i in range(N):
    if a[i]<min_value:
        min_value=a[i]

print(min_value)