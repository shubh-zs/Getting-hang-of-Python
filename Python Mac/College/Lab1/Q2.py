#To perform matrix multiplication 

try : 
    r1,w1,r2,w2 = map(int, input("Input the values for the dimentions of the matrices in the following format also the matrix dim. must be less than 3 \n" 
                    "\t\t:- Row1,Height1,Row2,Height2\n").strip().split(","))
    if(r2==w1):
        mat1 = [[0]*w1]*r1
        mat2 = [[0]*w2]*r2
        mat3 = [[0]*w2]*r1
        print("Input the values for the matrix1\n")
        for i in range(r1):
            for j in range(w1):
                mat1[i][j] = int(input())

        print("Input the values for the matrix2\n")
        for i in range(r2):
            for j in range(w2):
                mat2[i][j] = int(input())

        #Code that multiplies the two input matrice
        for i in range(r1):
            for j in range(w2):
                for k in range(w1):
                    mat3[i][j] += mat1[i][k]*mat2[k][j]
        

        print("The output is :\n")
        for i in range(r1):
            for j in range(w2):
                print(mat3[i][j]," ",end="")
            print()
    else:
        print("Matrix with input dimentions cannot multiply!!")

except ValueError:
    print("Value provided is not to the correct standard")



