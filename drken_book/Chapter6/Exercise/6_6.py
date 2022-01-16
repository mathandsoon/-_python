#章末問題6.6
#AtCoder Beginner Contest 026 D 高橋君ボール1号

from math import sin,pi

A,B,C=map(int,input().split())
left,right=0,300
while abs(A*left+B*sin(C*pi*left)-100)>10**(-8):
    mid=(left+right)/2
    if A*mid+B*sin(C*pi*mid)-100>0:
        right=mid
    else: left=mid

print(left)