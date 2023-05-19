# print the prime number in between the input range
st = 5
ls = 5
if(st<=ls):
    for i in range(1,11):
        f=0
        for j in range(2,i):
            if(i%j==0): 
                f=1 
                break
        if(f==0 and i>1): 
            print(i)


else: 
    print("Invalid Input")