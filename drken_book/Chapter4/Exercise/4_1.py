#章末問題4.1

def tribo(N):
    if N==0: return 0
    elif N==1: return 0
    elif N==2: return 1

    return tribo(N-1)+tribo(N-2)+tribo(N-3)