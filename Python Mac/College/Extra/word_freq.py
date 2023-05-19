from collections import Counter

a = "hi im krishna assistant, krishna aggarwal is krishna 's full name and krishna has a ring and krishna sits on the last bench"

a = a.split()
 
b = Counter(a)
b = max(list(b.items()),key= lambda x: x[1])
print(b[0],b[1],sep=" ")