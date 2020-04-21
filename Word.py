s=input()
u=0
l=0
for i in s:
    if(ord(i)>=65 and ord(i)<=90):
        u+=1
    else:
        l+=1
if(l>=u):
    for i in range(len(s)):
        if(ord(s[i])>=65 and ord(s[i])<=90):
            s=s[:i]+chr(ord(s[i])+32)+s[i+1:]
            

else:
    for i in range(len(s)):
        if(ord(s[i])>=97 and ord(s[i])<=122):
            s=s[:i]+chr(ord(s[i])-32)+s[i+1:]
            

print(s)




