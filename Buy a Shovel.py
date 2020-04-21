n,k=map(int,input().split())
for i in range(1,10):
    rem=(n*i)%10
    if(rem==0 or rem==k):
        print(i)
        break
