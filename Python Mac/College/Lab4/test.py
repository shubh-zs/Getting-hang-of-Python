a = [[6, 5, 3],[1,2,3],[1,8,5]]
def min_idx(ar :dict,not_idx :int = -1) ->int:
    min,idx = 999999,0
    for i,v in ar.items():
        if not_idx!=-1 and i == not_idx:
            continue
        if min > v:
            idx = i
            min = v
        # print(min,v,sep=" : ")
    return idx


cols = [[13, 27, 89, 96, 23, 22, 81, 82, 53],
    [40, 83, 53, 29, 37, 71, 84, 72, 38],
    [18, 75, 72, 37, 62, 72, 71, 27, 9]]


# cols= [[cols[j][i] for j in range(len(cols))] for i in range(len(cols[0]))]
# # cols = [[17,2,17],[16,16,5],[14,3,19]]

# for i in cols:
#     print(i)
# print()


l = cols[1]
l.sort(reverse=True)
print(l)

