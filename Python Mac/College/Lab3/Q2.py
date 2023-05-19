# To write a python program to find exponentiation (power of a number).

from cmath import log10

base = int(input("Input the number that is the base : "))
ans = int(input("Input the number after calculation : "))

precision = 10 ** (-5)
a = log10(ans)/log10(base)
a = float(str(a).split("+")[0][1:])

if((a-int(a))<precision):
    print(a)
else:
    print("Not a exponent of ",base)



