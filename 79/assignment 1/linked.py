class Node(object):
    def __init__(self, value):
        self.value = value
        self.next = None


node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node5 = Node(5)

node1.next=node4
node2.next = node5
node4.next = node2
node5.next=node3

node6=node1
while(node6.next!=None):
    node6=node6.next;
    print(node6.value)