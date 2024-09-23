import os
import pickle
class Node(object):
    def __init__(self, value):
        self.value = value
        self.next = None


class myQueue(object):
    
    def __init__(self):
        self.head = None
        self.tail = None
        self.sizea=0
    
    def enque(self,value):
        self.sizea += 1
        if self.head is None:
            self.head = value
            self.tail = self.head
        else:
            self.tail.next = value
            self.tail = self.tail.next
            self.tail.next=self.head

    def deque(self):

        
        if self.head==None:
            print("Queue is Empty")
            return None
        else:
            self.sizea-=1
            temp=self.head
            self.head=self.head.next;
            self.tail.next=self.head
            return temp


    def peek(self):
        if self.head==None:
            print("Empty Queue")
            return
        return self.head

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
    
        