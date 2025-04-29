class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None
        
class DoubleLinkedList:
    def __init__(self):
        self.head = self.tail = None
    
    def pushFront(self,e):
        new_node = Node(e)
        if self.head is None:
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
    
    def pushBack(self,e):
        new_node = Node(e)
        if self.tail is None:
            self.head = self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
    
    def popFront(self):
        if self.head is None:
            return None
        removed_node = self.head
        self.head = self.head.next
        if self.head is not None:
            self.head.prev = None
        else:
            self.tail = None
        return removed_node.data
    
    def popBack(self):
        if self.tail is None:
            return None
        removed_node = self.tail
        self.tail = self.tail.prev
        if self.tail is not None:
            self.tail.next = None
        else:
            self.head = None
        return removed_node.data
    
    def insertAtPosition(self, pos, e):
        if pos < 0:
            return
        new_node = Node(e)
        if pos == 0:
            self.pushFront(e)
            return
        current = self.head
        for _ in range(pos - 1):
            if current is None:
                return
            current = current.next
        if current is None:
            self.pushBack(e)
        else:
            new_node.next = current.next
            new_node.prev = current
            if current.next is not None:
                current.next.prev = new_node
            current.next = new_node
            if new_node.next is None:
                self.tail = new_node
            
    def removeAtPosition(self, pos):
        if pos < 0 or self.head is None:
            return
        if pos == 0:
            self.popFront()
            return
        current = self.head
        for _ in range(pos):
            if current is None:
                return
            current = current.next
        if current is None:
            return
        if current.prev is not None:
            current.prev.next = current.next
        if current.next is not None:
            current.next.prev = current.prev
        if current == self.tail:
            self.tail = current.prev
        if current == self.head:
            self.head = current.next
        del current
    
    def printDLL(self):
        current = self.head
        while current:
            print(current.data, end='<->')
            current = current.next
        print(None)
        
if __name__=="__main__":
    dll = DoubleLinkedList()
    dll.pushFront(10)
    dll.pushFront(20)
    dll.pushFront(30)
    dll.pushFront(40)
    dll.printDLL() # Output: 40<->30<->20<->10<->None
    
    dll.pushBack(50)
    dll.pushBack(60)
    dll.pushBack(70)
    
    dll.printDLL() # Output: 40<->30<->20<->10<->50<->60<->70<->None
    
    dll.popFront()
    dll.printDLL() # Output: 30<->20<->10<->50<->60<->70<->None
    
    dll.popBack()
    dll.printDLL() # Output: 30<->20<->10<->50<->60<->None