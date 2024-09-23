import os
import Queue1

class Node(object):
    def __init__(self,name,id,serv):
        self.id=id;
        self.name=name
        self.next=next
        self.ser=serv
        
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
ll = Queue1.Qea
try:
    savefile1=open(file="s2.pickle",mode="rb")
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
            a=Node(name,id,name2)
            ll.add(a)
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
            with open(file="s2.pickle",mode="wb")as savefile1:
                pickle.dump(ll,savefile1)
            stop = 1
        case _:
            print("Enter Correcgt Value")

