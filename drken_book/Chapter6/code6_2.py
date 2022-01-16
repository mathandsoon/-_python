#一般化した二分探索法の基本形

#xが条件を満たすかどうか
def P(x):
    return """TrueまたはFalse"""

#P(x)=Trueとなる最小の整数xを返す
def binary_search():
    left,right= #P(left)=False,P(right)=Trueとなるように

    while right-left>1:
        mid=left+(right-left)//2
        if P(mid): right=mid
        else: left=mid

    return right