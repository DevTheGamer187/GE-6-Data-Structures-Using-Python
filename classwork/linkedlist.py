class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        
class LinkedList:
    def __init__(self):
        self.head=None
    
    def insertAtBeg(self,ndata):
        new_node = Node(ndata)
        new_node.next = self.head
        self.head = new_node
    
    def instertAtEnd(self,ndata):
        new_node = Node(ndata)
        if self.head is None:
            self.head = new_node
            return
        temp=self.head
        while temp.next is not None:
            temp=temp.next
        temp.next=new_node
        return
    
    def displayList(self):
        temp=self.head
        while temp:
            print(temp.data,end=" ")
            temp=temp.next
        print()
        
if __name__=="__main__":
    
    newlist=LinkedList()
    
    newlist.insertAtBeg(3)
    newlist.insertAtBeg(7)
    newlist.insertAtBeg(9)