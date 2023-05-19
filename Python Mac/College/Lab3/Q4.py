# Tic-Tac-Toe Logic

board = [["O","#","O"],["X","O","#"],["X","#","O"]]

cxr = cxc = cor = coc = cxd = cod = 0
for i in range(3):
    for j in range(3):
        #Row Wise Checking
        if(board[i][j]=="X"):
            cxr += 1
        elif(board[i][j]=="O"):
            cor += 1
        
        #Col Wise Checking
        if(board[j][i]=="X"):
            cxc += 1
        elif(board[j][i]=="O"):
            coc += 1

for i in range(3):
    if(board[i][i]=="X"):
        cxd += 1
    elif(board[i][i]=="O"):
        cod += 1
        # print(i," ",j)
        # print(j," ",i)
if(cxr==3 or cxr == 3 or cxd == 3):
    print("X won")
elif(cor==3 or cor == 3 or cod == 3):
    print("O won")
else:
    print("noone won")
