#章末問題3.7
#Atcoder Beginner Contest 045 C たくさんの数式

"""実装方法2:+で区切った式を文字列として保持"""

S=input()

N=len(S)-1
ans=0
for bit in range(1<<N):
    formula=""
    for i in range(N):
        if bit>>i & 1:
            formula+=S[i]
            formula+="+"
        else:
            formula+=S[i]
    formula+=S[-1]
    ans+=eval(formula)

print(ans)