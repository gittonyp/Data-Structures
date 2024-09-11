import os
import pickle
import copy
import subprocess as sp
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Stack1:
    def __init__(self):
        self.topp = None
        self.size = 0

    def push(self, value):
        newnode = Node(value)
        if self.topp is None:

            self.topp = newnode
            self.size += 1
            return newnode
        else:
            temp = self.topp
            self.topp = newnode
            self.topp.next = temp
            self.size += 1

    def pop(self):
        if self.size == 0:
            raise Exception("Stack is empty")
        else:
            self.topp = self.topp.next
            self.size -= 1


    def top(self):
        if self.size == 0:
            raise Exception("Stack is empty")
        else:
            print(self.topp.value)


class todo:
    def __init__(self):
        self.ll=Stack1()
        self.mm=Stack1()
        self.bb=Stack1()

    def add(self, task):
        c=int(input("Enter Importance"))
        if c==0:
            self.ll.push(task)
        elif c==1:
            self.mm.push(task)
        elif c==2:
            self.bb.push(task)
        else:
            print("Invalid Input")

    def delete(self):
        if self.bb.size == 0:
            if self.mm.size == 0:
                self.ll.pop()
            else:
                self.mm.pop()
        else:
            self.bb.pop()

    def display(self):
        if self.bb.size == 0:
            if self.mm.size == 0:
                if self.ll.size == 0:
                    print("Stack is empty")
                else:
                    self.ll.top()
            else:
                self.mm.top()
        else:
            self.bb.top()
    def fullist(self):
        n=0
        b1 = copy.copy(self.bb)
        b2 = copy.copy(self.ll)
        b3 = copy.copy(self.mm)
        if b1.size != 0:
            while b1.size !=0:
                print(n, end=" ")
                b1.top()
                b1.pop()

                n+=1
        if b3.size != 0:
            while b3.size !=0:
                print(n, end=" ")
                b3.top()
                b3.pop()
                n += 1
        if b2.size != 0:
            while b2.size !=0:
                print(n, end=" ")
                b2.top()
                b2.pop()
                n += 1

    def exit(self):
        todol = open('todo.txt', 'wb')
        pickle.dump((self.bb.to_list(), self.mm.to_list(), self.ll.to_list()), todol)
        todol.close()

    def retrive(self):
        try:
            with open('todo.txt', 'rb') as todol:
                self.bb, self.mm, self.ll = pickle.load(todol)
        except FileNotFoundError:
            print("No saved data found.")



def TodoList():
    print("To Do List")
    print()
    print("1 Task list")
    print("2 Add Task")
    print("3 Remove Task")
    print("4 Full Task List")
    print("5 Retrive Data")
    print("6 Exit")


stop = 0
ll = todo()
while stop == 0:
    TodoList()
    choice = int(input("Enter"))

    temp=sp.call('cls', shell=True)
    match choice:
        case 1:
            ll.display()
        case 2:
            name = input("Enter Task Name: ")
            ll.add(name)

        case 3:
            ll.delete()
        case 4:
            ll.fullist()
        case 6:
            ll.exit()
            stop=1
        case 5:
            ll.retrive()
        case _:
            print("Enter Correcgt Value")



