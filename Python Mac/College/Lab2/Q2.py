# To get most frequent words in a texxt file

hash_dict = {}

y = []
with open("temp.txt","r") as file:
    
    lines = file.readlines()
    # print(lines)
    if lines:
        for x in lines: 
            y.extend(x.split(" "))
            # y.extend(list(map(chk , x)))
            
    else:
        print("The input file is empty")
        exit(0)
print(y)
for i in y:
    if i not in hash_dict:
        hash_dict[i] = 1
    else: hash_dict[i] +=1

while " " in hash_dict:
    hash_dict.pop(" ")
while "\n" in hash_dict:
    hash_dict.pop("\n")

freq = max(hash_dict.items(), key=lambda x: x[1])
print(freq)

# print("The word with most frequency : \"",freq[1][0],"\" with the frequency : ",freq[1][1])





