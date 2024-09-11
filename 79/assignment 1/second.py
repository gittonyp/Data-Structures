
import os
class Noode(object):

    def __init__(self, name, quantity, price):
        self.name = name
        self.nextt = None
        self.backk=None
        self.quantity = quantity
        self.price = price

class linked():
    head = None
    tail = None
    size = 0

    def add(self, name, quantity, price):
        newnode = Noode(name, quantity, price)
        self.size += 1
        if self.head == None:
            self.head = newnode
            self.tail = newnode
            newnode.nextt = newnode
            newnode.backk = newnode
        else:
            newnode.backk=self.tail;
            self.tail.nextt = newnode
            self.tail = newnode
            newnode.nextt = self.head;



    def print(self):
        print("Printing Order List")
        temp = self.head

        for i in range(0,self.size):
            print("Name: " + temp.name + " Price: " + temp.price + " Quantity: " + temp.quantity)
            temp = temp.nextt

    def remove(self):
        print("Enter Order Name")
        no = input()
        i = 0
        temp = self.head
        for j in range(0, self.size):
            if temp.name == no:
                i = 1
                break
            temp = temp.nextt
        if i==1:
            if self.head == temp:
                self.head = self.head.nextt
            temp1=temp.backk
            temp1.nextt=temp.nextt
            self.size-=1




    def update(self):
        print("Enter Order Name")
        no = input()
        i = 0
        temp = self.head
        for j in range(0, self.size):
            if temp.name == no:
                i=1
                break
            temp = temp.nextt
        if i==1:
            price = input("Enter price: ")
            quantity = input("Enter Quantity: ")
            temp.price = price
            temp.quantity = quantity

    def search(self):
        print("Enter Order Name")
        no = input()

        temp = self.head
        for j in range(0, self.size):
            if no==temp.name:
                print(" Name: " + temp.name + " Quantity: " + temp.quantity + " Price: " + temp.price)
            temp = temp.nextt





def Godown():
    print("Godown Management")
    print()
    print("1 Order list")
    print("2 Add Order")
    print("3 Search Order")
    print("4 Update Order Info")
    print("5 Remove Order")
    print("6 Exit")


stop = 0
ll = linked()
while stop == 0:
    Godown()
    choice = int(input("Enter"))
    os.system('cls')
    match choice:
        case 1:
            ll.print()
        case 2:
            name = input("Enter Name: ")
            quantity = input("Enter Quantity: ")
            price = input("Enter Price: ")
            ll.add(name, quantity, price)

        case 3:
            ll.search()
        case 4:
            ll.update()
        case 6:
            stop = 1
        case 5:
            ll.remove()
        case _:
            print("Enter Correcgt Value")

