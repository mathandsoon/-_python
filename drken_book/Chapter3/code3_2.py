#特定の要素の存在する「添字」も取得する

#入力を受け取る
N,v=map(int,input().split())
a=list(map(int,input().split()))

#線形探索
found_id=-1 #初期値は-1などありえない値に
"""C++とは異なりPythonでは-1をキーにして参照しても
配列の一番最後の要素が参照され、
エラーにならないため扱いには注意"""

for i in range(N):
    if a[i]==v:
        found_id=i #見つかったら添字を記録
        break #ループを抜ける

#結果出力(-1のときは見つからなかったことを表す)
print(found_id)