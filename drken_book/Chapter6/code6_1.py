#配列から目的の値を探索する二分探索法

N=8
a=[3,5,8,10,14,17,21,39]

#目的の値 key の添え字を返す（存在しない場合は-1）
def binary_search(key):
    left,right=0,len(a)-1 #配列aの左端と右端
    while right>=left:
        mid=left+(right-left)//2 #区間の真ん中
        if a[mid]==key: return mid
        elif a[mid]>key: right=mid-1
        elif a[mid]<key: left=mid+1

    return -1

print(binary_search(10))   #3
print(binary_search(3))    #0
print(binary_search(39))   #7

print(binary_search(-100)) #-1
print(binary_search(9))    #-1
print(binary_search(100))  #-1  