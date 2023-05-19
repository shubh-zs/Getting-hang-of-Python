# import pywhatkit as pwk
# i = 0
# for _ in ["+917011709833","+919582566693"]:
#     pwk.sendwhatmsg_instantly(_,"This is a computer generated message", tab_close= True, close_time = 3)
#     if(_=="+917011709833"): i +=1


# def rec(arr: list):
#     if(len(arr) != 0):
#         p = t.pop(0)
#         arr.insert(0,rec(arr))
#         return p
#     else: 
#         return 

# t = [1,2,3,4]    #its a stack with stkp at 1
# rec(t)
# print("final : ",t)
# for i in range(3):
#     for j in range(3):
#         if(i!=j):
#             continue
#         print(i,j)

# To change the value of a specific key in n number of dictionaries present in list
# nums = [{1:2,2:{3:1,4:5},4:8},{1:5,2:{3:1,4:5},4:8},{1:2,2:{3:1,4:5},4:8}]
# dick = {"t":[1,2,3,4],"e":[1,2,3,4],"s":[1,2,3,4]}
# k = 3

# for i,v in dick.items():
#     print(i,":",v[:k],end=", ")



from collections import Counter
 
# Creation of a Counter Class object using
# a string as an iterable data container
# Example - 1
a = Counter("geeksforgeeks")
 
# Elements of counter object
for i,j in a.items():
    print ( i,":",j, end = ", ")
print()