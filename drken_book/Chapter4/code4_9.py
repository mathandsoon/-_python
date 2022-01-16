#部分和問題を再帰関数を用いる全探索で解く

"""データ型が明示されていないため分かりづらいが、
関数 func は、i,w:整数, a:配列 が想定されている。"""
def func(i,w,a):
    #ベースケース
    if i==0:
        if w==0:
            return True
        else:
            return False
    
    #a[i-1]を選ばない場合
    if func(i-1,w,a): return True

    #a[i-1]を選ぶ場合
    if func(i-1,w-a[i-1],a): return True

    #どちらも False の場合は False
    return False

#入力
N,W=map(int,input().split())
a=list(map(int,input().split()))

#再帰的に解く
if func(N,W,a): print("Yes")
else: print("No")