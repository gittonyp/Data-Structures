import os
import pickle
class Node(object):
    def __init__(self, value):
        self.value = value
        self.next = None


class Q(object):
    sizea=0
    def __init__(self):
        self.head = None
        self.tail = None
    def add(self,value):
        self.sizea += 1
        if self.head is None:
            self.head = Node(value)
            self.tail = self.head
        else:
            self.tail.next = Node(value)
            self.tail = self.tail.next

    def remove(self):

        
        if self.head==None:
            print("Queue is Empty")
            return
        else:
            self.sizea-=1
            self.head=self.head.next;



    def print(self):
        temp= self.head
        while temp!=None:
            print(temp.value)
            temp = temp.next

    def top(self):
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
ll = Q()
with open(file="abc.pickle",mode="rb")as savefile1:
    ll=pickle.load(savefile1)
while stop == 0:
    Queue11()
    choice = int(input("Enter"))
    os.system('clear')
    match choice:
        case 1:
            Value = input("Enter Value: ")
            ll.add(Value)
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
            with open(file="abc.pickle",mode="wb")as savefile1:
                pickle.dump(ll,savefile1)
            stop = 1
        case _:
            print("Enter Correcgt Value")

