s=input()
s=s.replace('WUB',' ')
i=0
while(s[i]==' '):
    i+=1
s=s[i:]
s=s[::-1]
i=0
while(s[i]==' '):
    i+=1
s=s[i:]
s=s[::-1]
print(s)