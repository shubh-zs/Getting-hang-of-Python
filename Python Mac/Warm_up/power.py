inp = [1,2,3,4]
l = len(inp)

out_mat = [[]]

for i in range(1,2**l):
    ar1 = []
    j=i
    c=0
    while(j>0):
        if(j&1): ar1.append(inp[c])
        c=c+1
        j=int(j/2)
    out_mat.append(ar1)
print(out_mat)

