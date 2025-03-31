class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.head = None
    
    def insert(self, x):
        new_node = Node(x)
        if not self.head:
            self.head = new_node
            new_node.next = self.head
        else:
            temp = self.head
            while temp.next != self.head:
                temp = temp.next
            temp.next = new_node
            new_node.next = self.head
    
    def remove(self, x):
        if not self.head:
            return
        temp, prev = self.head, None
        while True:
            if temp.data == x:
                if prev:
                    prev.next = temp.next
                else:
                    last = self.head
                    while last.next != self.head:
                        last = last.next
                    self.head = temp.next if temp.next != temp else None
                    last.next = self.head
                return
            prev, temp = temp, temp.next
            if temp == self.head:
                break
    
    def search(self, x):
        temp = self.head
        if not temp:
            return None
        while True:
            if temp.data == x:
                return temp
            temp = temp.next
            if temp == self.head:
                break
        return None
    
    def display(self):
        if not self.head:
            return
        temp = self.head
        while True:
            print(temp.data, end=' -> ')
            temp = temp.next
            if temp == self.head:
                break
        print("(head)")

# Demonstration of CircularLinkedList
if __name__ == "__main__":
    cll = CircularLinkedList()
    
    print("Inserting elements:")
    cll.insert(10)
    cll.insert(20)
    cll.insert(30)
    cll.display()
    
    print("Removing element 20:")
    cll.remove(20)
    cll.display()
    
    print("Searching for element 30:")
    node = cll.search(30)
    print("Found" if node else "Not Found")