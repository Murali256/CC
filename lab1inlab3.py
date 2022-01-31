def dfs(matrix, x, y, n, m):
     
    if (x < 0 or y < 0 or
        x >= n or y >= m or
        matrix[x][y]!=1):
        return
        
    matrix[x][y] = 2

    dfs(matrix, x + 1, y, n, m);
    dfs(matrix, x, y + 1, n, m);
    dfs(matrix,x - 1, y, n, m);
    dfs(matrix,x, y - 1, n, m);
    return
N = int(input("Enter num of rows"))
M=int(input("Number of columns"))
matrix = []
for _ in range(N):
    matrix.append(list(map(int,input().split())))

result = 0
for i in range(N):
    for j in range(M):
             if (matrix[i][j] == 1):
                result += 1
                dfs(matrix,i, j, N, M)
 
print(result)