matrix = [[1,1,1],[1,0,1],[1,1,1]]

# In order to solve this question we need to mark the rows and columns with -1 or any other identifier , then set the rows and columns to 0

def markRows(matrix, n, m, i):
    for j in range(m):
        if matrix[i][j] != 0:
            matrix[i][j] = -1

def markCols(matrix, n, m, j):
    for i in range(n):
        if matrix[i][j] != 0:
            matrix[i][j] = -1

def setZeroes(matrix):
    n = len(matrix)
    m = len(matrix[0])
    
    for i in range(n):
        for j in range(m):
            if matrix[i][j] == 0:
                markRows(matrix, n, m, i)
                markCols(matrix, n, m, j)

    for i in range(n):
        for j in range(m):
            if matrix[i][j] == -1:
                matrix[i][j] = 0

setZeroes(matrix)

print(matrix)