#整数bit の表す部分集合にi番目の要素が含まれるかどうかを判定する

#bitを表す部分集合にi番目の要素が含まれる場合
if bit&(1<<i):

#含まれない場合
else:

"""
if (bit>>i)&1:
でもいい。体感的にはこっち使っている人の方が多い。"""