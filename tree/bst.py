import os

class Node(object):
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

class BST: 
    def __init__(self):
        self.root=None
    def insert(self,data):
        temp=self.root
        newnode=Node(data)
        if temp==None:
            self.root=newnode
        else:
            while temp!=None:
                if temp.left!=None and newnode.data<temp.data:
                    temp=temp.left
                    continue
                if temp.right!=None and newnode.data>=temp.data:
                    temp=temp.right
                    continue
                break
            if newnode.data<temp.data:
                temp.left=newnode
            else:
                temp.right=newnode
    
    def search(self,data):
        temp=self.root
        if temp==None:
            print("Empty Tree")
        else:
            while temp!=None:
                if temp.data==data:
                    print("Found Data")
                    return
                if temp.left!=None and data<temp.data:
                    temp=temp.left
                    continue
                if temp.right!=None and data>temp.data:
                    temp=temp.right
                    continue
                break
        print("Data Not Found")
    
    def delete(self,data):
        temp=self.root
        st=[]
        if temp==None:
            print("Empty Tree")
        else:
            st.append(self.root)
            while temp!=None:
                if temp.data==data and st.:
                    print("Found Data")
                    return
                if temp.left!=None and data<temp.data:
                    temp=temp.left
                    continue
                if temp.right!=None and data>temp.data:
                    temp=temp.right
                    continue
                break
        print("Data Not Found")
    
    def __proorderin(self,temp):
        if temp==None:
            return
        print(temp.data,end=" ")
        self.__proorderin(temp.left)
        self.__proorderin(temp.right)
    
    def preorder(self):
        temp=self.root
        self.__proorderin(temp)
        print()
        
    def __inorderin(self,temp):
        if temp==None:
            return
        
        self.__inorderin(temp.left)
        print(temp.data,end=" ")
        self.__inorderin(temp.right)
    
    def inorder(self):
        temp=self.root
        self.__inorderin(temp)
        print()
    
    def __postoderin(self,temp):
        if temp==None:
            return
        
        self.__postoderin(temp.left)
        
        self.__postoderin(temp.right)
        print(temp.data,end=" ")
    
    def postoder(self):
        temp=self.root
        self.__postoderin(temp)
        print()

    def interpreorder(self):
        print()
        temp=self.root
        if temp==None:
            print("Empty Tree")
        else:
            st=[]
            st.append(temp)
            while len(st)!=0:
                temp=st.pop()
                print(temp.data,end=" ")
                
                if temp.right!=None:
                    st.append(temp.right)
                if temp.left!=None:
                    st.append(temp.left)
                
                
    
    
    
tree=BST()
tree.insert(10)
tree.insert(5)
tree.insert(20)
tree.insert(3)
tree.insert(9)
tree.insert(15)
tree.insert(25)

tree.preorder()
tree.interpreorder()
tree.preorder()