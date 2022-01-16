#ユークリッドの互除法によって最大公約数を求める

def GCD(m,n):
    #ベースケース
    if n==0:
        return m
    
    #再帰呼び出し
    return GCD(n,m%n)


print(GCD(51,15)) #3が出力される
print(GCD(15,51)) #3が出力される