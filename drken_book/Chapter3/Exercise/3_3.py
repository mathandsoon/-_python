#章末問題3.3

N=int(input())
a=list(map(int,input().split()))

smallest=max(a[0],a[1])
second_smallest=min(a[0],a[1])
for i in range(2,N):
    if a[i]<=smallest:
        smallest,second_smallest=a[i],smallest
    elif smallest<a[i]<second_smallest:
        second_smallest=a[i]

print(second_smallest)