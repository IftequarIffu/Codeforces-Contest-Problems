n=int(input())
arr=list(map(int,input().split()))
r=0
c=0
co=0
for i in range(n):
    if(arr[i]==-1):
        c+=1
        if(r<c):
            co+=1
        else:
            r=r-1
            c=c-1
    else:
        c=0
        r=r+arr[i]
print(co)
