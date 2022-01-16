#章末問題4.2

def tribo(N):
    T=[0 for _ in range(N+1)]
    if N>=2: T[2]=1

    for i in range(3,N+1):
        T[i]=T[i-1]+T[i-2]+T[i-3]
    return T[N]

"""range(a,b)はa>=bのとき実行されないので、
場合分けは不要。"""