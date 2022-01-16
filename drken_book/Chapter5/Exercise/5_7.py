#章末問題5.7
#AtCoder Educational DP Contest F LCS

s=input()
t=input()
dp=[[0]*(len(t)+1) for _ in range(len(s)+1)]

for i in range(len(s)):
    for j in range(len(t)):
        if s[i]==t[j]:
            dp[i+1][j+1]=dp[i][j]+1
        else:
            dp[i+1][j+1]=max(dp[i][j+1],dp[i+1][j])

Ans=""
sl,tl=len(s),len(t)
while len(Ans)<dp[-1][-1]:
    if dp[sl][tl]==dp[sl-1][tl-1]+1 and s[sl-1]==t[tl-1]:
        sl-=1
        tl-=1
        Ans+=s[sl]
    elif sl>1 and dp[sl-1][tl]==dp[sl][tl]:
        sl-=1
    else: tl-=1

print(Ans[::-1])