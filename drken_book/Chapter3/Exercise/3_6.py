#章末問題3.6
#Atcoder Beginner Contest 051 B Sum-of-Three-Integers

K,S=map(int,input().split())

ans=0
for x in range(K+1):
    for y in range(K+1):
        if 0 <= S-x-y <= K:
            ans+=1

print(ans)