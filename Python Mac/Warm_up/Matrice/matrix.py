st = input().split()
inp1 = int(st[0])
inp2 = int(st[1])
print("Input this number of elements : ",inp1*inp2)

inp_arr = [int(x) for x in input().split()]
if(len(inp_arr)==inp1*inp2):
    mat = []
    out_mat = []
    c=0
    for a in range(inp1):
        ar1 = []
        for b in range(inp2):
            ar1.append(inp_arr[c])
            # print(c)
            c+=1
        mat.append(ar1)
    print(mat)
    

    for a in range(inp2):
        ar1 = []
        for b in range(inp1):
            ar1.append(mat[b][a])
        out_mat.append(ar1)
    
    for a in range(inp2):
        ar1 = []
        for b in range(inp1):
            print(out_mat[a][b],end=" ")
        print()
    
else:
    print(-1)

