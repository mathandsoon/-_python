#章末問題6.3
#第7回JOI 本選 問3 ダーツ
#https://atcoder.jp/contests/joi2008ho/tasks/joi2008ho_c

"""半分全列挙というアルゴリズムを用いる。"""
N,M=map(int,input().split())
P=[]
for i in range(N):
    P.append(int(input()))

P.append(0)
S=[]
for i in range(len(P)):
    for j in range(i,len(P)):
        S.append(P[i]+P[j])

S.sort()
ans=0
for s in S:
    b=M-s
    left,right=0,len(S)-1
    if S[left]>b: break
    elif S[right]<=b:
        ans=max(ans,S[right]+s)
    else:
        while right-left>1:
            mid=(left+right)//2
            if S[mid]<=b: left=mid
            else: right=mid
        ans=max(ans,S[left]+s)

print(ans)

"""
このアルゴリズムで正解だが、
AtCoderではPythonだと時間切れになり、
PyPy3だとメモリを使いすぎて正解にならない。
そこで二分探索法に関する標準ライブラリである
bisectをインポートして高速化したものを
6_3_2.pyに記した。
（標準ライブラリはC言語で処理されるので高速になる。
ただし、使用されるアルゴリズムはここで示したものと同等なものである。）
"""