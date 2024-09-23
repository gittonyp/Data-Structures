import os
import pickle
class customer(object):
    def __init__(self, n,i,s):
        self.name=n;
        self.id=i;
        self.service=s;


class Qea(object):
    
    def __init__(self):
        self.head = None
        self.tail = None
        self.sizea=0
    def add(self,value):
        self.sizea += 1
        if self.head is None:
            self.head = value
            self.tail = self.head
        else:
            self.tail.next = value
            self.tail = self.tail.next
            self.tail.next=self.head

    def remove(self):

        
        if self.head==None:
            print("Queue is Empty")
            return
        else:
            self.sizea-=1
            self.head=self.head.next;
            self.tail.next=self.head



    def print(self):
        temp= self.head
        for i in range(0,self.sizea):
            print(temp.value)
            temp = temp.next

    def top(self):
        if self.head==None:
            print("Empty Queue")
            return
        print(self.head.value)
        return

    def isEmpty(self):
        if self.head==None:
            return True
        else:
            return False
    def isFull(self):
        try:
            newnode=Node(10)
        except MemoryError:
            return True
        else:
            return False
    
        

def Queue11():
    print("Queue")
    print()
    print("1 Add")
    print("2 Remove")
    print("3 isEmpty")
    print("4 isFull")
    print("5 Print Top")
    print("6 Print Full Queue")
    print("7 Exit")


stop = 0
ll = Qea()

while stop == 0:
    Queue11()
    choice = int(input("Enter"))
    os.system('clear')
    match choice:
        case 1:
            Value = input("Enter ID: ")
            name=input("Enter Name")
            ser=input("Enter Service")
            Val=object(Value,name,ser)
            ll.add(Val)
        case 2:
            ll.remove()

        case 3:
            
            if ll.isEmpty():
                print("Empty")
            else:
                print("Not empty")
        case 4:
            if ll.isFull():
                print("Full")
            else:
                print("Not Full")
        case 5:
            ll.top() 
        case 6:
            ll.print()
        case 7:
            
            stop = 1
        case _:
            print("Enter Correcgt Value")

