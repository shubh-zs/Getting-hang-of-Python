from math import *
from random import *
from collections import Counter

a = ["act","god","cat","dog","tac"]
   
a = list(set(a))

max_len = len(max(a,key= lambda x: len(x)))
b = [[]]*max_len

for i in a:
    b[len(i)-1].append(i)

print(b)
       
       
       
   
   
       
   
   
   
       
       
       
   
       
       
       
       
       
   
       
   
       
   
    
   
       
   
   
   
       
       
       
   
   
       
   
   
   
   
   
   
   
   
   
       
   