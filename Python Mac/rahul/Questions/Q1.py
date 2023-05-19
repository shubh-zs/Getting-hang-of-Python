# given a list count the numbers

lis = [1,2,"hello",12.23,"ssss",17]
def l(x):
    if(type(x)==type(9)): return True
a = 0
for i in lis:
    if(l(i)):
        a+=1
print(a)