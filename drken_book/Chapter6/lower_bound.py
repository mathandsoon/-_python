"""
std:lower_boundに対応した関数です。
自前のものと標準ライブラリのものを紹介します。
"""

"""std:lower_boundの対応物"""
def lower_bound(key,a):
    left,right=0,len(a)-1
    if a[right]<key: return len(a)
    while right-left>1:
        mid=(left+right)//2
        if a[mid]<key: left=mid
        else: right=mid
    return right

"""標準ライブラリの利用の場合"""
from bisect import bisect_left

"""help関数で関数の内容を参照できる"""
print(help(bisect_left))