arr=list(map(int,input().split()))
s=input()
c=0
for i in s:
    c=c+arr[int(i)-1]

print(c)
