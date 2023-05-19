
print("The Calculator has begun")

b = 1
while b:
    print("\n\n\t\tThe Operations : \n 1. Addition \n 2. Subtraction \n 3. Division \n 4. Multiplication")
    opr = int(input("Provide Input for the Operation "))
    
    i1,i2 = map(int,input("Input the two values : ").split(" "))
    
    if(opr==1): c = i1+i2
    elif(opr==2): c = i1-i2
    elif(opr==3): c = i1/i2
    elif(opr==4): c = i1*i2

    print("The output of the operation of operands ",c)
else:
    print("End")