# Returns the number of correct spellings provided by the user

spell = {"Spell": "S", 
         "BUSINESS":"BISINESS",
         "WINDOWS":"WINDMILL", 
         "WERE":"WEAR", 
         "SAMPLE":"SAMPLE"
        }
out_lis = [0,0,0]

for i,v in spell.items():
    if i==v:
        out_lis[0]+=1
    elif len(i)!=len(v):
        out_lis[2]+=1
    else:
        wr_cr = p = f = 0

        while(p<len(i)):
            if(i[p]!=v[p]):
                wr_cr+=1
            if(wr_cr>2):
                f=1
                break
            p+=1
        if f: out_lis[2]+=1
        else: out_lis[1]+=1


print(out_lis)

        

            

