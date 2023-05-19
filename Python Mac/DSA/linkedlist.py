class node:
    def __init__(self,data,next=None) -> None:
        self.data = data
        self.next = next
    
    def display(self):
        n = self
        while n:
            print(n.data)
            n=n.next
    
    def insert(self,m,n):
        if(m==None or n==None): print("Insufficient Input")
        else:
            n.next=m.next
            m.next=n
def init():
    global start,end
    start=end=None

def insert_first():
    global start , end
    data = int(input("Please enter the input for the node : "))
    if(start==None): 
        start = node(data)
        end = start
    else:
        n = node(data)
        start.insert(n,start)
        start=n

def insert_last():
    global start , end

    data = int(input("Please enter the input for the node : "))
    if(start==None): start=end= node(data)
    else:
        n = node(data)
        start.insert(end,n)
        end=n

def delete_first() -> int:
    global start , end

    if start==None: return None
    else:
        n = start.data
        start = start.next
        if start==None: 
            end=None
        return n

def delete_last():
    global start , end

    if end==None: 
        return None
    elif end==start: 
        n = end.data
        end=start=None
    else:
        no = start
        while no.next != end: 
            no = no.next
        end=no
        if start==None: end=None
    return n



if __name__ == "__main__":
    init()
    insert_first()
    insert_first()
    start.display()
    insert_first()
    start.display()
    insert_last()
    start.display()
    print(delete_first())
    start.display()
    print(delete_last())
    start.display()

    