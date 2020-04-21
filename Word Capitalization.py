s=input()
if(ord(s[0])>=97 and ord(s[0])<=122):
    s=chr(ord(s[0])-32)+s[1:]

print(s)