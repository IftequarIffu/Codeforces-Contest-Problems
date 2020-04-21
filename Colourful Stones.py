s=input()
t=input()
ind=0
for i in range(len(t)):
    if(t[i]==s[ind]):
        ind+=1

print(ind+1)



