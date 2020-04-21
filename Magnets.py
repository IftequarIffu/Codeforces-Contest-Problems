n=int(input())
arr=[]
for _ in range(n):
    arr.append(input())
c=0
for i in range(n-1):
    if(arr[i]!=arr[i+1]):
        c+=1

print(c+1)

    