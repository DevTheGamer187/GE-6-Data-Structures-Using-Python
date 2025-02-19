class Queue:
    def __init__(self, max_cap):
        self.queue_items = []  
        self.size = 0
        self.capacity = int(max_cap)
        self.front = 0

    def enqueue(self, item):
        if self.size == self.capacity:
            print("Queue is full")
        else:
            self.queue_items.append(item)
            self.size += 1

    def dequeue(self):
        if self.is_empty():
            print("Queue is empty")
            return None
        else:
            item = self.queue_items[self.front]
            self.front += 1
            self.size -= 1
            if self.front > len(self.queue_items) // 2:
                self.queue_items = self.queue_items[self.front:]
                self.front = 0
            return item

    def front_element(self):
        if self.is_empty():
            print("Queue is empty")
            return None
        else:
            return self.queue_items[self.front]

    def is_empty(self):
        return self.size == 0

    def get_size(self):
        return self.size

    def display(self):
        if self.is_empty():
            print("Queue is empty")
        else:
            print("Queue:", self.queue_items[self.front:self.front + self.size])

q = Queue(3)
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)

print("Front element:", q.front_element())
print("Queue size:", q.get_size())  # Changed from q.size() to q.get_size()

q.display()

print("Dequeued:", q.dequeue())
print("Queue size after dequeue:", q.get_size())  # Changed here as well

q.display()

print("Is queue empty?", q.is_empty())

q.enqueue(40)  
print("Queue size after attempting to enqueue when full:", q.get_size())  # And here

q.display()