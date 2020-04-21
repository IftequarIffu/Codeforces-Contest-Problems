n=int(input())
arr=[]
for _ in range(n):
    arr.append(list(map(int,input().split())))
c=0
for i in range(n-1):
    for j in range(i+1,n):
        if(arr[i][0]==arr[j][1] and arr[i][1]==arr[j][0]):
            c+=2
        elif(arr[i][0]!=arr[j][1] and arr[i][1]==arr[j][0]):
            c+=1
        elif(arr[i][0]==arr[j][1] and arr[i][1]!=arr[j][0]):
            c+=1

print(c)


