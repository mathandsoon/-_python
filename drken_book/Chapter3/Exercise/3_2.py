#章末問題3.2

N,v=map(int,input().split())
a=list(map(int,input().split()))

count=0
for i in range(N):
    if a[i]==v:
        count+=1

print(count)