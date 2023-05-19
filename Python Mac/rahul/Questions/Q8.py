# Multippy all the elements with 10

lis1 = [1,2,"o",12,"ssss",17,123,12324]

for i in range(len(lis1)): 
    if isinstance(lis1[i],int):
        lis1[i] = lis1[i]*10

print(lis1)