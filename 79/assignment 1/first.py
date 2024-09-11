import os


class Noode(object):

    def __init__(self, name, age, disease):
        self.name = name
        self.nextt = None
        self.age = age
        self.disease = disease


class linked():
    head = None
    tail = None
    size = 0

    def add(self, name, age, disease):
        newnode = Noode(name, age, disease)
        self.size += 1
        if self.head == None:
            self.head = newnode
            self.tail = newnode
        else:
            self.tail.nextt = newnode
            self.tail = newnode

    def addfirst(self, name, age, disease):
        newnode = Noode(name, age, disease)
        self.size += 1
        if self.head == None:
            self.head = newnode
            self.tail = newnode
        else:
            newnode.nextt = self.head
            self.head = newnode

    def removefirst(self):
        temp = self.head
        self.head = self.head.nextt
        temp.nextt = None
        self.size -= 1

    def addb(self, name):
        name2 = input("Enter Name: ")
        age = input("Enter Age: ")
        disease = input("Enter Disease: ")
        newnode = Noode(name2, age, disease)

        if self.head == None:
            self.head = newnode
            self.tail = newnode
        else:
            temp = self.head
            while temp != None:
                temp = temp.nextt
                i += 1

                if temp.name == name:
                    newnode.nextt = temp.nextt
                    temp.nextt = newnode
                    return
        self.size += 1

    def print(self):
        print("Printing Patient List")
        temp = self.head

        while temp != None:
            print("Name: " + temp.name + " Age: " + temp.age + " Disease: " + temp.disease)
            temp = temp.nextt

    def search(self):
        print("Enter Patient Name")
        no = input()

        temp = self.head
        while temp != None:
            if temp.name == no:
                print(" Name: " + temp.name + " Age: " + temp.age + " Disease: " + temp.disease)
                return
            temp = temp.nextt

    def update(self):
        print("Enter Patient Name")
        no = input()
        i = 1
        temp = self.head
        while temp != None:
            if temp.name == no:
                break
            temp = temp.nextt

        age = input("Enter Age: ")
        disease = input("Enter Disease: ")
        temp.age = age
        temp.disease = disease


def Hospital():
    print("Hospital Management")
    print()
    print("1 Patient list")
    print("2 Add Patient")
    print("3 Emergency Patient")
    print("4 Search Patient")
    print("5 Update Patient Info")
    print("6 Remove Patient")
    print("7 Add Between")
    print("8 Exit")


stop = 0
ll = linked()
while stop == 0:
    Hospital()
    choice = int(input("Enter"))
    os.system('cls')
    match choice:
        case 1:
            ll.print()
        case 2:
            name = input("Enter Name: ")
            age = input("Enter Age: ")
            disease = input("Enter Disease: ")
            ll.add(name, age, disease)

        case 3:
            name = input("Enter Name: ")
            age = input("Enter Age: ")
            disease = input("Enter Disease: ")
            ll.addfirst(name, age, disease)
        case 4:
            ll.search()
        case 5:
            ll.update()
        case 8:
            stop = 1
        case 6:
            ll.removefirst()
        case 7:
            print("Enter After which patient To add")
            name = input()
            ll.addb(name)
        case _:
            print("Enter Correcgt Value")
