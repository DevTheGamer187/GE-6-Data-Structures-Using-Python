class Node:
    def __init__(self,element,next):
        self.element = element
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = self.tail = None
        
    def push_Front(self,e): #O(1)
        if self.tail is None:
            self.head = Node(e,self.head)
            self.tail = self.head
            return self.head.element
        else:
            new_node = Node(e, self.head)
            self.head = new_node
            return self.head.element
    
    def push_Back(self,e): #O(1)
        if self.tail is None:
            self.head = Node(e,self.head)
            self.tail = self.head
            return self.head.element
        else:
            new_node = Node(e, None)
            self.tail.next = new_node
            self.tail = new_node
            return self.tail.element
    
    def pop_Front(self): #O(1)
        if self.head is None:
            raise Exception("List is empty")
        else:
            removed_element = self.head.element
            self.head = self.head.next
            if self.head is None:
                self.tail = None
            return removed_element
        
    def pop_Back(self): #O(n)
        if self.head is None:
            raise Exception("List is empty")
        elif self.head == self.tail:
            removed_element = self.head.element
            self.head = self.tail = None
            return removed_element
        else:
            current = self.head
            while current.next != self.tail:
                current = current.next
            removed_element = self.tail.element
            current.next = None
            self.tail = current
            return removed_element
        
    def insertAtPosition(self, e, pos): #O(n)
        if pos < 0:
            raise Exception("Invalid position")
        elif pos == 0:
            self.push_Front(e)
        else:
            current = self.head
            for _ in range(pos - 1):
                if current is None:
                    raise Exception("Position out of bounds")
                current = current.next
            new_node = Node(e, current.next)
            current.next = new_node
            if new_node.next is None:
                self.tail = new_node

    def searchLinkedList(self, e): #O(n)
        current = self.head
        index = 0
        while current:
            if current.element == e:
                print(index)
                return
            current = current.next
            index += 1
        print(-1)
    
    def printLL(self): #O(n)
        current = self.head
        while current:
            print(current.element, end=" -> ")
            current = current.next
        print("None")
    
if __name__ == "__main__":
    ll = LinkedList()
    ll.push_Front(1)
    ll.push_Front(2)
    ll.push_Front(3)
    
    ll.printLL()  
    
    ll.insertAtPosition(4,1)
    
    ll.searchLinkedList(2)
    
    ll.printLL()
    
    print("new_outputs")
    
    ll.push_Back(4)
    ll.push_Back(5)
    ll.push_Back(6)

    ll.printLL()
    
    ll.pop_Front()
    ll.pop_Back()
    ll.printLL()  
