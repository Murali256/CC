l1=[]
def sort(l):
    if(isEmpty(l)==0):
        l1.append(max(l))
        l.remove(max(l))
        sort(l)
    else:
        return
def isEmpty(l):
    if(len(l)==0):
        return 1
    else:
        return 0
l=list(map(int,input().split( )))
sort(l)
print(l1)