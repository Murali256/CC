s=input()
l=len(s)
m=[]
for j in range(l-1):
    k=[]
    for i in range(j,l):
        if s[i] not in k:
            k.append(s[i])
        else:
            break;
    m.append(k)
maxi=0
for i in range(len(m)):
    if(len(m[i])>maxi):
        maxi=len(m[i])
print(maxi)