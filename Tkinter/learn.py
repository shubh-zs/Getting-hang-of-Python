from math import *
from posixpath import split
from re import L
from tkinter import *
root = Tk()
root.geometry("400x300")
e = Entry(root,width=60)

a=0
def ins(num):
    global a,x
    e.insert(a,num)
    if(num in ["sin()","cos()","tan()","log()","dec ","bin ","oct "]):
        a += 4
    else: 
        a +=1
    if(o01["state"]==DISABLED and num == ","): 
        com()
    if(o01["text"]=="10" and num !=","):
        x = int(num)
        eva()
        

# When clr is clicked
def opr1():
    global a
    e.delete(0,END)
    a = 0

#When del is clicked 
def opr2():
    global a
    e.delete(a-1,a)
    a -=1

# When = is clicked
def opr3():
    global a
    b = (eval(str(e.get()),{"sin":sin,"cos":cos,"tan":tan,"log":log}))
    # patani kya likha hua tha
    #   ["state"] = DISABLED  
    e.delete(0,END)#ye bhi
    e.insert(0,str(b))
    a = len(e.get())



# When = is clicked
def spl2():
    global a
    a += 4
    b = e.get()
    d = 0
    for i in ["dec ","bin ","oct "]:
        if(i==b[:4]): 
            d+=1
    return d

def eva():
    global a
    rev_com()   
    b = e.get()
    c = spl2()
    d = b.split(",")
    e.delete(0,END)

    if(c==1):
        e.insert(0,int(d[0],x))
    elif(c==2):
        if(x == 2):
            e.insert(0,d[0])
        elif(x==10):
            temp = bin(d[0])
        elif(x==8):
            temp = int(d[0],8)
            temp = bin(temp)
        else:
            print("BASE Error")
        e.insert(0,temp[2:])
        
    elif(c==8):
        if(x==8):
            e.insert(0,d[0])
        elif(x==10):
            e.insert(0,oct(d[0])[2:])
        elif(x==2):
            temp = int(d[0],2)
            temp = oct(temp)
            e.insert(0,oct(d[0])[2:])
        else:
            print("BASE Error")
            
    else: 
        print("Eval base Error",c,b[4:])
        exit()

def com():
    b0["state"] = DISABLED    
    b1["state"] = DISABLED
    b2["state"] = DISABLED
    b3["state"] = DISABLED
    b4["state"] = DISABLED
    b5["state"] = DISABLED
    b6["state"] = DISABLED
    b7["state"] = DISABLED
    b8["state"] = DISABLED
    b9["state"] = DISABLED
    o01["state"]= NORMAL
    o02["state"]= NORMAL
    o03["state"]= NORMAL
    o01.config(text="10",command=lambda: ins("10"))
    o02.config(text="8",command=lambda: ins("8"))
    o03.config(text="2",command=lambda: ins("2"))

# When Base is clicked
def spl():
    e.delete(0,END)
    a = 0
    o01["state"]= DISABLED
    o02["state"]= DISABLED
    o03["state"]= DISABLED
    o04["state"]= DISABLED
    o05["state"]= DISABLED
    o06["state"]= DISABLED
    o07["state"]= DISABLED
    o08["state"]= DISABLED
    o13.grid_remove()
    w3.config(command=eva)

# When Back is clicked
def spl1():
    global a
    e.delete(0,END)
    a = 0
    o00["state"]= NORMAL
    o01["state"]= NORMAL
    o02["state"]= NORMAL
    o03["state"]= NORMAL
    o04["state"]= NORMAL
    o05["state"]= NORMAL
    o06["state"]= NORMAL
    o07["state"]= NORMAL
    o08["state"]= NORMAL
    o13.grid(row=3,column=4)
    w3.config(command=opr3)
    rev_com()

# for to reerse the acrtions of comma
def rev_com():
    b0["state"] = NORMAL    
    b1["state"] = NORMAL
    b2["state"] = NORMAL
    b3["state"] = NORMAL
    b4["state"] = NORMAL
    b5["state"] = NORMAL
    b6["state"] = NORMAL
    b7["state"] = NORMAL
    b8["state"] = NORMAL
    b9["state"] = NORMAL
    o01.config(text=  "+",command=lambda: ins("+"))
    o02.config(text=  "-",command=lambda: ins("-"))
    o03.config(text=  "x",command=lambda: ins("*"))
    



b0 = Button(root, text = "0", padx = 20 , pady=20,command=lambda: ins("0"))#0
b1 = Button(root, text = "1", padx = 20 , pady=20,command=lambda: ins("1"))#1
b2 = Button(root, text = "2", padx = 20 , pady=20,command=lambda: ins("2"))#2
b3 = Button(root, text = "3", padx = 20 , pady=20,command=lambda: ins("3"))#3
b4 = Button(root, text = "4", padx = 20 , pady=20,command=lambda: ins("4"))#4
b5 = Button(root, text = "5", padx = 20 , pady=20,command=lambda: ins("5"))#5
b6 = Button(root, text = "6", padx = 20 , pady=20,command=lambda: ins("6"))#6
b7 = Button(root, text = "7", padx = 20 , pady=20,command=lambda: ins("7"))#7
b8 = Button(root, text = "8", padx = 20 , pady=20,command=lambda: ins("8"))#8
b9 = Button(root, text = "9", padx = 20 , pady=20,command=lambda: ins("9"))#9

w1 = Button(root, text = "Clear",padx = 20 ,pady=20,command= opr1)#clr
w2 = Button(root, text = "Delete",padx = 20 ,pady=20,command=opr2)#del
w3 = Button(root,text="=",padx = 20 ,pady=20,command = opr3)#eval

f = Frame(root)
global o00,o01
o00 = Button(root, text=  ",",padx = 20 ,pady=20,command=lambda: ins(","))#,
o01 = Button(root, text=  "+",padx = 20 ,pady=20,command=lambda: ins("+"))#+  
o02 = Button(root, text=  "-",padx = 20 ,pady=20,command=lambda: ins("-"))#-  
o03 = Button(root, text=  "x",padx = 20 ,pady=20,command=lambda: ins("*"))#x  
o04 = Button(root, text=  "/",padx = 20 ,pady=20,command=lambda: ins("/"))#/ 
o05 = Button(root, text="sin",padx = 20 ,pady=20,command=lambda: ins("sin()"))#sin
o06 = Button(root, text="cos",padx = 20 ,pady=20,command=lambda: ins("cos()"))#cos
o07 = Button(root, text="tan",padx = 20 ,pady=20,command=lambda: ins("tan()"))#tan
o08 = Button(root, text="log",padx = 20 ,pady=20,command=lambda: ins("log()"))#log

o09 = Button(f, text="dec",padx = 10 ,pady=5,command=lambda: ins("dec "))#dec
o10 = Button(f,text="bin", padx = 10 ,pady=5,command=lambda: ins("bin "))#bin
o12 = Button(f,text="oct",padx = 10 ,pady=5,command=lambda:  ins("oct "))#oct
o13 = Button(root,text="Base",padx = 30 ,pady=20,command= spl)#Base
o14 = Button(f,text="Back",padx = 10 ,pady=5,command=spl1)#Back

# f.destroy()                

# l.pack()
e.grid(row=0,column=0,columnspan=6)
b1.grid(row=1,column=0)
b2.grid(row=1,column=1)
b3.grid(row=1,column=2)
b4.grid(row=2,column=0)
b5.grid(row=2,column=1)
b6.grid(row=2,column=2)
b7.grid(row=3,column=0,rowspan=2)
b8.grid(row=3,column=1,rowspan=2)
b9.grid(row=3,column=2,rowspan=2)
b0.grid(row=5,column=0)

w1.grid(row=5,column=4)
w2.grid(row=5,column=5)
w3.grid(row=5,column=2)

o00.grid(row=5,column=1)#,
o01.grid(row=1,column=3)#+  
o02.grid(row=2,column=3)#-  
o03.grid(row=3,column=3,rowspan=2)#x  
o04.grid(row=5,column=3)#/  
o05.grid(row=1,column=4)#sin
o06.grid(row=1,column=5)#cos
o07.grid(row=2,column=4)#tan
o08.grid(row=2,column=5)#log
f.grid(row=3,column=4,rowspan=2,columnspan=2)
o09.grid(row=3,column=4)#dec
o10.grid(row=3,column=5)#bin
o12.grid(row=4,column=5)#oct
o13.grid(row=3,column=4,rowspan=2,columnspan=2)#base
o14.grid(row=4,column=4)#back



root.mainloop()