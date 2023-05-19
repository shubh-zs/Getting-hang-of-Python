# To write a python program of linear search.
l  = int(input("Input the length of array : "))
mat = [0]*l
print("Input the values : ")
for i in range(l):
    mat[i] = int(input())

t = int(input("Input the target element : "))
for i in range(len(mat)):
    if((t^mat[i])==0):
        print("Element Found at : ",i)
        i=-1
        break
if i!=-1:
    print("Not Found")
