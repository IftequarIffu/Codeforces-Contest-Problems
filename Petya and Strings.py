s1=input()
s2=input()
for i in range(len(s1)):
    if(ord(s1[i])>=65 and ord(s1[i])<=90):
        s1=s1[:i]+chr(ord(s1[i])+32)+s1[i+1:]

for i in range(len(s2)):
    if(ord(s2[i])>=65 and ord(s2[i])<=90):
        s2=s2[:i]+chr(ord(s2[i])+32)+s2[i+1:]

for i in range(len(s1)):
    if(ord(s1[i])<ord(s2[i])):
        print(-1)
        break
    elif(ord(s1[i])>ord(s2[i])):
        print(1)
        break
else:
    print(0)
