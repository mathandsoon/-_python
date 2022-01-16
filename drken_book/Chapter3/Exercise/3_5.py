#章末問題3.5
#Atcoder Beginner Contest 081 B Shift-Only

N=int(input())
a=list(map(int,input().split()))

ans=0
while True:
    pos=True
    for i in range(N):
        if a[i]%2==0:
            a[i]/=2
        else:
            pos=False
            break
    if pos:
        ans+=1
    else:
        break

print(ans)