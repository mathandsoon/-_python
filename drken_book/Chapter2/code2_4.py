#最近点対問題に対する全探索

def calc_dist(x1,y1,x2,y2):
    return ((x1-x2)**2+(y1-y2)**2)**0.5

N=int(input())
x,y=[],[]
for i in range(N):
    X,Y=map(int,input().split())
    x.append(X)
    y.append(Y)

minimum_dist=10000000000

for i in range(N):
    for j in range(N):
        dist_i_j=calc_dist(x[i],y[i],x[j],y[j])
        if dist_i_j<minimum_dist:
            minimum_dist=dist_i_j

print(minimum_dist)