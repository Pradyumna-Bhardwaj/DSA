matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
zeroes = []
for row in range(len(matrix)):
    for column in range(len(matrix[0])):
        if(matrix[row][column] == 0):
            zeroes.append([row,column])
# print(zeroes)
for zc in range(len(zeroes)):
    for column in range(len(matrix[0])):
        matrix[zeroes[zc][0]][column] = 0
    for row in range(len(matrix)):
        matrix[row][zeroes[zc][1]] = 0
# print(matrix)
# for zr in range(len(zeroes)):
    
print(matrix)