arr1=[int(x) for x in input().split()]
arr2=[int(x) for x in input().split()]
count=0
for i in arr2:
    if i in arr1:
        count+=1
if(count==len(arr2)):
    print("arr2 is a subset of arr1")
else:
    print("arr2 is not a subset of arr1")

