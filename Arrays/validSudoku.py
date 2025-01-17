board = [["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]

# row check
res = True
rowCheck = {str(i): 0 for i in range(1,10)}
rowCheck["."] = 0
for i in range(len(board)):
    for key in rowCheck:
            rowCheck[key] = 0
    for j in range(len(board)):
        rowCheck[board[i][j]]+=1
        if(rowCheck[board[i][j]]>1 and board[i][j] != "."):
            res = False
# column check
columnCheck = {str(i): 0 for i in range(1,10)}
columnCheck["."] = 0
for i in range(len(board)):
    for key in columnCheck:
            columnCheck[key] = 0
    for j in range(len(board)):
        columnCheck[board[j][i]]+=1
        if(columnCheck[board[j][i]]>1 and board[j][i] != "."):
            res = False
# box check
boxCheck= {str(i): 0 for i in range(1,10)}
boxCheck["."] = 0
for i in[0,3,6]:
    for j in [0,3,6]:
        b=0
        for key in boxCheck:
            boxCheck[key] = 0
        while(b<3):
            a = 0
            while(a<3):
                boxCheck[board[i+b][j+a]]+=1
                if(boxCheck[board[i+b][j+a]]>1 and board[i+b][j+a] != "."):
                    res = False
                a+=1
            b+=1
print(res)

            