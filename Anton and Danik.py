n=int(input())
s=input()
a=0
d=0
for i in s:
    if(i=='A'):
        a+=1
    else:
        d+=1

if(a>d):
    print("Anton")
elif(d>a):
    print("Danik")
else:
    print('Friendship')

