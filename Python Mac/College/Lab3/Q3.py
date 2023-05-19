# Restaurant data with Tuple, and how to change if called for

dishes = ("Oyster","Sushi","Caviar","Butter Chicken","Ramen")
passw  = "1a2b3c" 

def show(dishes : tuple):
    print("The Dishes this restaurant Offers : ")
    for i in dishes:
        print(i)
    print("Thats all")
    return

def modify(dishes : tuple, ind : int):
    dish = input("Input the dish name :  ")
    try: 
        dishes[ind] = dish
    except TypeError:
        print("Error, Try again with password")

def modmodify(dishes : tuple, ind : int):
    tryp = input("Input the Password :  ")
    if(tryp == passw):
        dish = input("Input the dish name :  ")
        dishes = list(dishes)
        try :
            dishes[ind] = dish
            show(dishes)
        except IndexError:
            print("Input Index Out of Range")
    else:
        print("Error, Wrong password")

i = 1
while i:
    print("\n\nInput Choice : \n  0. Exit \n  1. Show\n  2. Modify\n  3. Modify with Password : ")
    i = int(input())
    if i==1:
        show(dishes)
    elif i==2:
        ind = int(input("Input the Index : "))
        modify(dishes, ind)
    elif i==3:
        ind = int(input("Input the Index : "))
        modmodify(dishes,ind)





    
