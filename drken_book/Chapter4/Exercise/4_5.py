#章末問題4.5
#AtCoder Beginner Contest 114 C 755

N=int(input())
Answer=set()

def SFT(N,cur,use):
    if cur>N: return 
    
    if use==7:
        Answer.add(cur)
    sft=[3,5,7]
    for i in range(3):
        SFT(N,cur*10+sft[i],use|(1<<i))

    return 

SFT(N,0,0)
print(len(Answer))

"""
関数SFTの引数useは3,5,7の各数が使われたかの判定用。
二進数表示で、
3が使われた->2^0の位が1
5が使われた->2^1の位が1
7が使われた->2^2の位が1
となっている。"""