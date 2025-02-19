class Queue:
    def __init__(self,max_cap):
        self.queue_items=[None]
        self.size=0
        self.capacity=int(max_cap)
        self.front=0

    def enqueue(self, item):
        if self.size==self.capacity:
            print("Queue is full")
            return
        else:
            self.queue_items.append(item)

    def dequeue(self):
        if self.is_empty():
            print("Queue is empty")
            return
        else:
            print(self.queue_items[self.front])
            for i in range(1,self.size):
                self.queue_items[i-1]=self.queue_items[i]
            self.size=-1
            self.queue_items[self.size]=None
            return
        
    def front(self):
        if not self.is_empty():
            print("Queue is empty")
        else:
            print(self.queue_items[self.front])

    def is_empty(self):
        return len(self.queue) == 0

    def size(self):
        return len(self.queue)

# Example usage
q = Queue()
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)

print("Front element:", q.front())
print("Queue size:", q.size())

print("Dequeued:", q.dequeue())
print("Queue size after dequeue:", q.size())

print("Is queue empty?", q.is_empty())
