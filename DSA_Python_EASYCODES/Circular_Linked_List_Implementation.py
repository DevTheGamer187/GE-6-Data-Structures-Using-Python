class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    
class CircularLinkedList:
    def __init__(self):
        self.head = self.tail = None
        
    def insertAtHead(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = self.tail = new_node
            new_node.next = new_node
        else:
            new_node.next = self.head
            self.tail.next = new_node
            self.head = new_node
        
    def insertAtTail(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = self.tail = new_node
            new_node.next = new_node
        else:
            self.tail.next = new_node
            new_node.next = self.head
            self.tail = new_node
            
    def deleteAtHead(self):
        if self.head is None:
            return
        if self.head == self.tail:
            self.head = self.tail = None
        else:
            self.tail.next = self.head.next
            self.head = self.head.next
            
    def deleteAtTail(self):
        if self.head is None:
            return
        if self.head == self.tail:
            self.head = self.tail = None
        else:
            current = self.head
            while current.next != self.tail:
                current = current.next
            current.next = self.head
            self.tail = current
    
    def printCLL(self):
        if self.head is None:
            return
        current = self.head
        while True:
            print(current.data, end=" -> ")
            current = current.next
            if current == self.head:
                break
        print("(head)")

if __name__ == "__main__":
    cll = CircularLinkedList()
    cll.insertAtHead(1)
    cll.insertAtHead(2)
    cll.insertAtHead(3)
    cll.printCLL()  # Output: 3 -> 2 -> 1 -> (head)
    cll.insertAtHead(4)
    cll.printCLL()  # Output: 4 -> 3 -> 2 -> 1 -> (head)
    
    cll.insertAtTail(5)
    cll.insertAtTail(6)
    
    cll.printCLL() # Output: 4 -> 3 -> 2 -> 1 -> 5 -> 6 -> (head)
    
    cll.deleteAtHead()
    cll.printCLL()  # Output: 3 -> 2 -> 1 -> 5 -> 6 -> (head)
    
    cll.deleteAtTail()
    cll.printCLL()  # Output: 3 -> 2 -> 1 -> 5 -> (head)