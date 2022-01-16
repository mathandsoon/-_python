#章末問題6.2
#AtCoder Beginner Contest 077 C Snuke-Festival

N=int(input())
A=list(map(int,input().split()))
B=list(map(int,input().split()))
C=list(map(int,input().split()))

A.sort()
C.sort()
ans=0

for i in range(N):
    left,right=0,N-1
    if A[right]<B[i]:
        a=right
    elif A[left]>=B[i]:
        a=-1
    else:
        while right-left>1:
            mid=(left+right)//2
            if A[mid]>=B[i]: right=mid
            else: left=mid
        a=left
    
    left,right=0,N-1
    if C[left]>B[i]:
        c=left
    elif C[right]<=B[i]:
        c=N
    else:
        while right-left>1:
            mid=(left+right)//2
            if C[mid]<=B[i]: left=mid
            else: right=mid
        c=right
    
    ans+=(a+1)*(N-c)

print(ans)