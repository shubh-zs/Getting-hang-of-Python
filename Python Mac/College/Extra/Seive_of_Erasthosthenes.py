inp = int(input("Input the range : "))

#Modified algorithm that has less space complexity but high time complexity
# prime_mat = [2]
# s=2
# for i in range(3,inp,s):
#     f=1
#     s = s and i
#     for j in prime_mat:
#         if(i%j==0): f=0
#     if(f):
#         prime_mat.append(i) 
    
# print(prime_mat)


#Actual algoithm
prime_mat = [[i ,1] for i in range(2,inp)]
inp = len(prime_mat)

for i in range(inp):
    if prime_mat[i][1]:
        for j in range(i,inp,prime_mat[i][0]):
            if(i!=j and j<inp):
                prime_mat[j][1]=0

# print(prime_mat)
# time,space O(N)
for i,j in prime_mat:
    if(j):
        print(i)
