n,k=map(int,input().split())
arr=list(map(int,input().split()))
c=0
# tarr=[]
# for i in range(n):
#     if(i%2!=0):
#         if(c<=k):
#             tarr.append(arr[i]-1)
#             c+=1
#         else:
#             tarr.append(arr[i])
#     else:
#         tarr.append(arr[i])
# print(*tarr)

for i in range(n):
    if(i%2!=0):
        if(c<=k):
            print(arr[i]-1,end=' ')
            c+=1
        else:
            print(arr[i],end=' ')
    else:
        print(arr[i],end=' ')
print('')