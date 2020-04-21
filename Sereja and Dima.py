n=int(input())
arr=list(map(int,input().split()))
l=0
h=n-1
s=0
d=0
st=1
dt=0
while(l<=h):
    if(st>dt):
        if(arr[l]>arr[h]):
            s=s+arr[l]
            l=l+1
        else:
            s=s+arr[h]
            h=h-1
        dt=1
        st=0
    else:
        if(arr[l]>arr[h]):
            d=d+arr[l]
            l=l+1
        else:
            d=d+arr[h]
            h=h-1
        dt=0
        st=1

print(s,d)



