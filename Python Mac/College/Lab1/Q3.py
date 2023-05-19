'''
    Number of rows from user. Number of columns=number of rows +1. 
    Take m X n matrix. If any number is consecutive for three times either in rows, column, and diagonals then print the number. 
    If multiple numbers are there then print min of those.
'''

r = int(input("Provide the number og rows in the matrix : "))
c = r+1
mat= [[0]*c]*r
if(r>1):
    print("Input the values for the matrix\n")
    for i in range(r):
        for j in range(c):
            mat[i][j] = int(input())
    # mat = [[1,2,2,4],[1,2,3,4],[1,2,3,4]]
    repC= []
    repR= []
    
    #Column Wise Checking
    for j in range(c):
        i = 0
        tc = mat[i][j]
        fl = 1
        for a in range(3):
            if(i+a<r):
                if(tc!=mat[i+a][j]):
                    fl=0
                    break
            else:
                fl=0
        if(fl):
            repC.append(tc)
        i+=1

    #Row Wise Checking
    for i in range(r):
        j = 0
        tc = mat[i][j]
        fl = 1
        for a in range(3):
            if(i+a<c):
                if(tc!=mat[i][j+a]):
                    fl=0
                    break
            else:
                fl=0
        if(fl):
            repR.append(tc)
        j+=1
    
    mc = mr = None
    if(repC and repR):
        mc = min(repC)
        mr = min(repR)

    print("Value repeating 3 times in a column : ",mc," \n Value repeating 3 times in a Row : ",mr," \nDone")
    print("Repeating vals in col : ",repC,"Repeating vals in row : ",repR)
    
else: 
    print("Null")




