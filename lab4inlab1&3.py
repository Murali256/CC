def findMinCost(cost):
		
		if(len(cost)==0):
			return 0
		n=len(cost[0])
		m=len(cost)
		
		
		for i in range(1,n):
			cost[0][i]=cost[0][i-1]+cost[0][i]
		for i in range(1,m):
			cost[i][0]=cost[i-1][0]+cost[i][0]
			
		for i in range(1,m):
			for j in range(1,n):
				cost[i][j]=cost[i][j]+min(cost[i-1][j],cost[i][j-1])
	
		return cost[m-1][n-1]
n=int(input())
p=[]
for i in range(n):
   p.append(list(map(int,input().split())))
print(findMinCost(p))
print(p)
