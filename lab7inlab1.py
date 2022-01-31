import itertools

numbers = [int(x) for x in input().split()]
target = int(input())
r=[]
a=[]

result = [seq for i in range(len(numbers), 0, -1)
          for seq in itertools.combinations(numbers, i)
          if sum(seq) == target]
for i in result:
    i=list(i)
    i.sort()
    r.append(i)
for i in r:
    if i not in a :
        a.append(i)
    else:
        pass
    
print(a)
print(len(a))
    
