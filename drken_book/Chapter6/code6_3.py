#年齢当てゲームの実装

print("Start Game!")

#Aさんの数の候補を表す区間を、[left,right)と表す
left,right=20,36

#Aさんの数を1つに絞れないうちは繰り返す
while right-left>1:
    mid=left+(right-left)//2 #区間の真ん中

    #mid以上かを聞いて、回答をyes/noで受け取る
    print("Is the age less than {} ? (yes/no)".format(mid))
    ans=input()

    #回答に応じて、ありうる数の範囲を絞る
    if ans=="yes":
        right=mid
    else: left=mid

print("The age is {} !".format(left))