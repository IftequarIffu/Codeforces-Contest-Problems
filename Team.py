n=int(input())
arr=[]
c=0
for _ in range(n):
    arr.append(list(map(int,input().split())))
    
for i in range(len(arr)):
    co=0
    for j in range(len(arr[i])):
        if(arr[i][j]==1):
            co+=1
    if(co>=2):
        c+=1

print(c)