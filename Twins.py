# import math
n=int(input())
arr=list(map(int,input().split()))
s=sum(arr)
arr.sort(reverse=True)
i=0
c=0
for i in range(n):
    c=c+arr[i]
    if(c>(s/2)):
        break
print(i+1)

    
    

    