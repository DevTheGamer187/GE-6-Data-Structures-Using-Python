class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
    
    def insert_at_beginning(self, x):
        new_node = Node(x)
        if self.head:
            new_node.next, self.head.prev = self.head, new_node
        self.head = new_node
    
    def insert_at_end(self, x):
        new_node = Node(x)
        if not self.head:
            self.head = new_node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next, new_node.prev = new_node, temp
    
    def insert_at_position(self, x, pos):
        if pos == 0:
            self.insert_at_beginning(x)
            return
        new_node, temp = Node(x), self.head
        for _ in range(pos - 1):
            if not temp: return  # Position out of bounds
            temp = temp.next
        if temp:
            new_node.next, new_node.prev = temp.next, temp
            if temp.next:
                temp.next.prev = new_node
            temp.next = new_node
    
    def remove_from_beginning(self):
        if self.head:
            self.head = self.head.next
            if self.head:
                self.head.prev = None
    
    def remove_from_end(self):
        if not self.head:
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        if temp.prev:
            temp.prev.next = None
        else:
            self.head = None
    
    def remove_at_position(self, pos):
        if pos == 0:
            self.remove_from_beginning()
            return
        temp = self.head
        for _ in range(pos):
            if not temp: return  # Position out of bounds
            temp = temp.next
        if temp:
            if temp.next:
                temp.next.prev = temp.prev
            if temp.prev:
                temp.prev.next = temp.next
    
    def search(self, x):
        temp, index = self.head, 0
        while temp:
            if temp.data == x:
                return temp
            temp, index = temp.next, index + 1
        return None  # Element not found
    
    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end=' <-> ' if temp.next else '\n')
            temp = temp.next

# Demonstration of DoublyLinkedList
if __name__ == "__main__":
    dll = DoublyLinkedList()
    
    print("Inserting elements at the beginning:")
    dll.insert_at_beginning(10)
    dll.insert_at_beginning(20)
    dll.display()
    
    print("Inserting elements at the end:")
    dll.insert_at_end(30)
    dll.insert_at_end(40)
    dll.display()
    
    print("Inserting element at position 2:")
    dll.insert_at_position(25, 2)
    dll.display()
    
    print("Removing element from beginning:")
    dll.remove_from_beginning()
    dll.display()
    
    print("Removing element from end:")
    dll.remove_from_end()
    dll.display()
    
    print("Removing element from position 1:")
    dll.remove_at_position(1)
    dll.display()
    
    print("Searching for element 30:")
    node = dll.search(30)
    print("Found" if node else "Not Found")