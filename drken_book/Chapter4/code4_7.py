#フィボナッチ数列をfor文による反復で求める

F=[0 for _ in range(50)]
F[0],F[1]=0,1
for N in range(2,50):
    F[N]=F[N-1]+F[N-2]
    print("{} 項目: ".format(N,F[N]))