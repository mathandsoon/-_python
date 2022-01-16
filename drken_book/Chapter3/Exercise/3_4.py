#章末問題3.4

N=int(input())
a=list(map(int,input().split()))

ans=0
for i in range(N):
    for j in range(N):
        ans=max(ans,a[i]-a[j])

print(ans)