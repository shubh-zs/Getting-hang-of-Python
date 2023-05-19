# There are N houses. The amount to color each house with Red, Green, Blue colors is given. 
# Write a program to find the minimum amount to paint all houses such that no 2 adjacent houses have the same color.

# n = int(input("Input the number of houses : "))   #3

# returns the min element of the idx from dict O(1)
def min_idx(ar :dict,not_idx :int = -1) ->int:
    min,idx = 999999,0
    for i,v in ar.items(): #this would only work for 3 times and has no growth factor
        if not_idx!=-1 and i == not_idx:
            continue
        if min > v:
            idx = i
            min = v
        # print(min,v,sep=" : ")
    return idx

n=3
red  =  [6, 5, 3, 4]
green=  [3, 1, 6, 1]
blue =  [9, 4, 2, 1]

cols = [[6, 5, 3],
        [0, 1, 6],
        [9, 4, 2]]

cols = [red,green,blue]

cols = [[2],[3],[1]]


cols = [[13, 27, 89, 96, 23, 22, 81, 82, 53],
    [40, 83, 53, 29, 37, 71, 84, 72, 38],
    [18, 75, 72, 37, 62, 72, 71, 27, 9]]




cols= [[cols[j][i] for j in range(len(cols))] for i in range(len(cols[0]))]
# cols = [[17,2,17],[16,16,5],[14,3,19]]

for i in cols:
    print(i)
print()


min_mat = []

for i in range(len(cols)):    #n times
    print(cols[i])

    idx = min_idx(dict(enumerate(cols[i])))
    print("the chosen : ",cols[i][idx])
    sum = cols[i][idx]

    idxf = idxr = idx
    #The element has been chosen and the loop is divided into two partsm
    for k in range(i-1,-1,-1):
        idxr = min_idx(dict(enumerate(cols[k])),idxr)
        print("k : ",cols[k][idxr])
        sum += cols[k][idxr]

    for j in range(i+1,len(cols)):
        idxf = min_idx(dict(enumerate(cols[j])),idxf)
        print("j : ",cols[j][idxf])
        sum += cols[j][idxf]

    min_mat.append(sum)
    print("sum : ",sum)
    print()

print(min(min_mat))
        
        


    
    
        