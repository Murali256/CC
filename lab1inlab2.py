def st(s1,s2,s3):

    if(sum(s1)==sum(s2)==sum(s3)):
        return sum(s1)
    elif sum(s1)>=sum(s2) and sum(s1)>=sum(s3):
        s1.pop(0)
        return  st(s1,s2,s3)
    elif  sum(s2)>=sum(s3):
        s2.pop(0)
        return  st(s1,s2,s3)
    else:
        s3.pop(0)
        return  st(s1,s2,s3)
       
       
       
    
h=list(map(int,input().split()))
s1=list(map(int,input().split()))
s2=list(map(int,input().split()))
s3=list(map(int,input().split()))
print(st(s1,s2,s3))