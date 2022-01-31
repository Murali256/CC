n=int(input())
l=list(map(int,input().split()))
m=9999999
for i in range(len(l)):
    for j in range(i+1,len(l)):
        if(l[i]==l[j]):
            res=abs(i-j)
            if(res<m):
                m=res
if(len(l)==len(set(l))):
    print("-1")
else:
    print(m)
        
