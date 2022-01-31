t=int(input())
res=[]
while(t>0):
    n,x=map(int,input().split())
    array=[int(i) for i in input().split()][:n]
    l=list(set(array))
    if(len(l)==x):
        res.append("Good")
    elif(len(l)<x):
        res.append("Bad")
    else:
        res.append("Average")

    t-=1
for i in res:
    print(i)