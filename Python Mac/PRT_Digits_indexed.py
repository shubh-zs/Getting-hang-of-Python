from math import log10
#This programme will print any digit from the given integer indexing starting form back from 1 till the first digit 
#The same variables are used to reduce the usage of space.

i = int(input("Input the number : "))
j = int(log10(i))+1
# if(j%2!=0): j = j-1
for a in range(1,j+1):  
    b = i%(10**j)/10**(a)  #this number is the value but selected nymber is behind the decimal
    c = int((b-int(b))*10) #number form above is taken, subtracted and multiplied by 10 then we remove the deicmal part
    print(c)




# The OutPut is given by : 

# Input the number : 123456
# input should be less than equal to 6 : 1
# 6
