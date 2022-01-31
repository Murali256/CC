def wiggle(l):
    f1=-1
    C=1
    for i in range(len(l)-1):
        if f1==-1:
            if l[i]-l[i+1]>0:
                f1=0
                C+=1
            elif l[i]-l[i+1]<0:
                f1=1
                C+=1
        elif l[i]-l[i+1]>0 and f1==1 :
            f1=0
            C+=1
        elif l[i]-l[i+1]<0 and f1==0:
            f1=1
            C+=1
    return C
l=list(map(int,input().split(' ')))
print(wiggle(l))