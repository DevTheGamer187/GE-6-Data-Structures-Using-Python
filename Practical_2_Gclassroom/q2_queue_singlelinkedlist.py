class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.front = None  # Head of the queue
        self.rear = None   # Tail of the queue
    
    # Add element to the end (rear) - O(1)
    def enqueue(self, x):
        new_node = Node(x)
        if self.rear is None:  # If queue is empty
            self.front = new_node
            self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node
    
    # Remove element from the front - O(1)
    def dequeue(self):
        if self.front is None:  # If queue is empty
            return None
        removed = self.front.data
        self.front = self.front.next
        if self.front is None:  # If queue becomes empty
            self.rear = None
        return removed
    
    # Get front element without removing - O(1)
    def peek(self):
        if self.front is None:
            return None
        return self.front.data
    
    # Check if queue is empty - O(1)
    def is_empty(self):
        return self.front is None
    
    # Helper function to print queue (for testing)
    def print_queue(self):
        current = self.front
        if current is None:
            print("Queue is empty")
            return
        while current:
            print(current.data, end=" <- ")
            current = current.next
        print("Front")

# Example usage
if __name__ == "__main__":
    q = Queue()
    print("Is empty?", q.is_empty())  # True
    
    q.enqueue(1)  # 1
    q.enqueue(2)  # 1 <- 2
    q.enqueue(3)  # 1 <- 2 <- 3
    q.print_queue()  # 1 <- 2 <- 3 <- Front
    
    print("Front element:", q.peek())  # 1
    print("Dequeued:", q.dequeue())    # 1, queue: 2 <- 3
    q.print_queue()  # 2 <- 3 <- Front
    
    print("Dequeued:", q.dequeue())    # 2, queue: 3
    print("Dequeued:", q.dequeue())    # 3, queue: empty
    print("Is empty?", q.is_empty())   # True