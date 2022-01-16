#線形探索法

#入力を受け取る
N,v=map(int,input().split())
a=list(map(int,input().split()))

#線形探索
exist=False
for i in range(N):
    if a[i]==v:
        exist=True

#結果出力
if exist:
    print("Yes")
else:
    print("No")