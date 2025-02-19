class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.queue.pop(0)
        raise Exception("Queue is empty")

    def front(self):
        if not self.is_empty():
            return self.queue[0]
        raise Exception("Queue is empty")

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
