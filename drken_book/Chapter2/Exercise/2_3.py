#章末問題2.3

def is_prime(N):
    if N<=1:
        return False
    for p in range(2,int(N**0.5)+1):
        if N%p==0:
            return False
    return True