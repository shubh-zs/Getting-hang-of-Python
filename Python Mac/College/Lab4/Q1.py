# To write a python program to find the maximum of a list of numbers.
l  = int(input("Input the length of array : "))
mat = [0]*l
print("Input the values : ")
for i in range(l):
    mat[i] = int(input())

print("The maximum value is : ",max(mat))