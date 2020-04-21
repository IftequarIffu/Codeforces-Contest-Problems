s=input()
n=len(s)
for i in range(n):
    if(s[i]=='A' or s[i]=='E' or s[i]=='I' or s[i]=='O' or s[i]=='U' or s[i]=='Y' or s[i]=='a' or s[i]=='e' or s[i]=='i' or s[i]=='o' or s[i]=='u' or s[i]=='y'):
        s=s.replace(s[i],' ')
    
s=s.replace(' ','')




# print(s)
# for i in range(len(s)):
#     s=s[:i]+'.'+s[i:]
# print(s)
for i in range(len(s)):
    if(ord(s[i])>=65 and ord(s[i])<=90):
        s=s[:i]+chr(ord(s[i])+32)+s[i+1:]


# print(s)

t=''
for i in range(len(s)):
    t=t+'.'+s[i]

print(t)