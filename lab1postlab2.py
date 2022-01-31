s=[]
res=[]
def query(q):
    if len(q)==2:
         s.append(q[1])
    elif len(q)==1:
         if q[0]==2:
             s.pop()
         elif q[0]==3:
             r=max(s)
             res.append(r)
n=int(input())
for i in range(n):
  q=[int(a) for a in input().split()]
  query(q)
for i in res:
  print(i)