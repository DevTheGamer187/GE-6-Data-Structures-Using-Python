class Node:
    def __init__(self, element):
        self.element = element
        self.next = None
        
class Queue:
    def __init__(self):
        self.front = self.rear = None
        
    def is_empty(self):
        return self.front is None
    
    def enqueue(self, e):
        new_node = Node(e)
        if self.rear is None:
            self.front = self.rear = new_node
            return
        self.rear.next = new_node
        self.rear = new_node
        
    def dequeue(self):
        if self.is_empty():
            return None
        removed_element = self.front.element
        self.front = self.front.next
        if self.front is None:
            self.rear = None
        return removed_element
    
    def printQueue(self):
        if self.is_empty():
            print("Queue is empty")
            return
        current = self.front
        while current:
            print(current.element, end=" , ")
            current = current.next
        print()

if __name__=="__main__":
    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    queue.printQueue()  # Output: 1 , 2 , 3
    print(queue.dequeue())  # Output: 1
    print(queue.is_empty())  # Output: False
    queue.dequeue()
    queue.dequeue()
    print(queue.is_empty())  # Output: True
    print(queue.dequeue())  # Output: None
    queue.printQueue()  # Output: Queue is empty