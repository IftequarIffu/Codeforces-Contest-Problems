n=int(input())
arr=list(map(int,input().split()))
narr=[0]*n
for i in range(n):
    narr[arr[i]-1]=i+1
print(*narr)