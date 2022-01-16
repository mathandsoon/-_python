#再帰呼び出しが止まらない再帰関数

def func(N):
    if N==0: return 0
    return N+func(N+1)