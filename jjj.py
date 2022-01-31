l=[int(x) for x in input().split()]
i=1
if len(l)>=3:
    while(i+2<=len(l)):
        if(l[i-1]<l[i]>l[i+1]):
            print(l[i])
        i+=1