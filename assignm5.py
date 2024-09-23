import queueconstruct
import pickle
import os

class customer(object):
    def __init__(self, n,i,s):
        self.name=n;
        self.id=i;
        self.service=s;

def printQueuemenu():
    print("Customer List")
    print()
    print("1 Add")
    print("2 Remove")
    print("3 isEmpty")
    print("4 isFull")
    print("5 Print Customer")
    print("6 Exit")

class Assign():
    def __init__(self):
        self.usesr=queueconstruct.myQueue()
    
    def add(self):
        name=input("Enter Name")
        id=int(input("Enter Id"))
        service=input("Enter Service")
        val=customer(name,id,service)
        self.usesr.enque(val);
    
    def remove(self):
        self.usesr.deque()
    
    def isempty(self):
        return self.usesr.isEmpty()
    
    def isfull(self):
        return self.usesr.isFull()
    
    def print(self):
        a=self.usesr.peek()
        print(a.id,a.name,a.service)
    


stop = 0
ll = Assign()

while stop == 0:
    printQueuemenu()
    choice = int(input("Enter"))
    os.system('clear')
    match choice:
        case 1:
            ll.add()
        case 2:
            ll.remove()

        case 3:
            
            if ll.isempty():
                print("Empty")
            else:
                print("Not empty")
        case 4:
            if ll.isfull():
                print("Full")
            else:
                print("Not Full")
        case 5:
            ll.print() 
        case 6:
            with open(r"assign5dataq.pickle","wb") as file1:
                pickle.dump(ll,file1)
            stop = 1
        case _:
            print("Enter Correcgt Value")


        