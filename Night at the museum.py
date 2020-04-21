s=input()
index=97
c=0
for i in range(len(s)):
    tc=abs(ord(s[i])-index)
    if(tc>13):
        c=c+(26-tc)
    else:
        c=c+tc
    index=ord(s[i])

print(c)




