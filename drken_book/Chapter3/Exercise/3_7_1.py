#章末問題3.7
#Atcoder Beginner Contest 045 C たくさんの数式

"""実装方法1:区切った値をリストに格納する"""

S=input()

N=len(S)-1
ans=0
for bit in range(1<<N):
    front,end=0,0
    Number=[]
    for i in range(N):
        if bit>>i & 1:
            end=i+1
            Number.append(S[front:end])
            front=end
    Number.append(S[front:len(S)])
    ans+=sum(map(int,Number))

print(ans)