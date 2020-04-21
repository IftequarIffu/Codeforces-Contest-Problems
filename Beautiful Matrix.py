arr=[]
for _ in range(5):
    arr.append(list(map(int,input().split())))

c=0
for i in range(5):
    for j in range(5):
        if(arr[i][j]==1):
            c=1
            break
    if(c==1):
        break

print(abs(i-2)+abs(j-2))