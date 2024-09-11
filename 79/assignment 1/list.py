class Node(object):
    def __init__(self, value):
        self.value = value
        self.next = None


class linked(object):
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

    def addbetweem(self,value):
        self.sizea += 1
        if self.head is None:
            self.head = Node(value)
            self.tail = self.head
        else:
            temp = self.head
            while temp != None:

                if temp.value == value:
                    break
                temp = temp.next
            value = input()
            node = Node(value);
            node.next = temp.next
            temp.next = node



    def removeback(self):

        temp=self.head
        while temp.next.next!=None:
            temp = temp.next
        temp.next=None
        self.sizea=self.sizea-1



    def print(self):
        temp= self.head
        while temp!=None:
            print(temp.value)
            temp = temp.next
    def search(self,value):
        temp= self.head
        while temp!=None:
           if temp.value==value:
               return True
        return False

ll=linked()
ll.add(9)
ll.add(18)
ll.add(27)
ll.add(36)
ll.add(45)
ll.add(54)
ll.add(63)
ll.add(72)
ll.add(81)
ll.add(90)
ll.print()
# ll.removeback()
ll.addbetweem(63)
ll.print()

