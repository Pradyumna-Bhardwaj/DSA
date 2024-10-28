board = [["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]

# code not complete

columnCheck = 0*[9]
boxCheck = [0]*9
ans = []
for i in range(0,9):
    rowCheck = [0]*9
    for j in range(0,9):
        if(board[i][j] != "."):
            rowCheck[int(board[i][j])-1] += 1
    for it in range(len(rowCheck)):
        if(rowCheck[it]>1):
            ans.append(False)
        else:
            ans.append(True)

for j in range(0,9):
    columnCheck = [0]*9
    for i in range(0,9):
        if(board[i][j] != "."):
            columnCheck[int(board[i][j])-1] += 1
    # print(columnCheck)
    for it in range(len(columnCheck)):
        if(columnCheck[it]>1):
            ans.append(False)
        else:
            ans.append(True)
res = 'true'
for i in range(len(ans)):
    if(ans[i]==False):
        res = 'false'

print(res)
            