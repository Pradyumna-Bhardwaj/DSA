
# method 1  - best runtime but worst storage optimization
matrix = [[1,2,3],[4,5,6],[7,8,9]]
newMatrix = []
for j in range(len(matrix)):
    i = 0
    currEntry = [0]*len(matrix)
    for i in range(len(matrix)):
        currEntry[i] = matrix[len(matrix)-1-i][j]
    newMatrix.append(currEntry)
matrix = newMatrix.copy()
print(matrix)


# method 2 - by taking mirror image across diagnol then right most column (med. runtime + optimized storage)
# matrix = [[1,2,3],[4,5,6],[7,8,9]]
# for i in range(len(matrix)):
#     for j in range(i+1, len(matrix)):
#         varStore = matrix[i][j]
#         matrix[i][j] = matrix[j][i]
#         matrix[j][i] = varStore
