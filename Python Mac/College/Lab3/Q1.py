# calculating the square root by newton's method

def mySqrt(x):
    r = x
    precision = 10 ** (-10)
    while abs(x - r * r) > precision:
        r = (r + x / r) / 2
    if (r) < int(r)+precision:
        return int(r)
    return "Not a square root"

inp = int(input("Input the number to be calculated for : "))
x = (inp+(inp/inp))/2
print(mySqrt(inp))

# print("Final Ans : ",newton(inp,x))
# def newton(inp,x):
#     # print(x)
#     precision = 10 ** (-10)
#     while abs(x - x * x) > precision:
#         x= (x+inp/x)/2
#         return newton(inp,x)
#     else:
#         return x