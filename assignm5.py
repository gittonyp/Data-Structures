import os
import pickle
class Node(object):
    def __init__(self, id,name,service):
        self.id = id
        self.name=name
        self.service=service
        self.next = None


class Q(object):
    
    def __init__(self):
        self.head = None
        self.tail = None
        self.sizea=0
    def add(self,id,name,service):
        self.sizea += 1
        if self.head is None:
            self.head = Node(id,name,service)
            self.tail = self.head
        else:
            self.tail.next = Node(id,name,service)
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
            print(temp.id,temp.name,temp.service)
            temp = temp.next

    def top(self):
        if self.head==None:
            print("Empty Queue")
            return
        temp=self.head
        print(temp.id,temp.name,temp.service)
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
    print("Customer List")
    print()
    print("1 Add")
    print("2 Remove")
    print("3 isEmpty")
    print("4 isFull")
    print("5 Print Top")
    print("6 Print Full Queue")
    print("7 Exit")


stop = 0
ll = Q()
try:
    savefile1=open(file="as5.pickle",mode="rb")
    ll=pickle.load(savefile1)
except EOFError:
    print()
    
while stop == 0:
    Queue11()
    choice = int(input("Enter"))
    os.system('clear')
    match choice:
        case 1:
            id = int(input("Enter Id: "))
            name=input("Enter Name: ")
            name2=input("Enter Service: ")
            ll.add(id,name,name2)
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
            with open(file="as5.pickle",mode="wb")as savefile1:
                pickle.dump(ll,savefile1)
            stop = 1
        case _:
            print("Enter Correcgt Value")

