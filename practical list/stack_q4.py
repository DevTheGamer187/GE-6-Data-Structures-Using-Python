class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        return "Stack is empty"

    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        return "Stack is empty"

    def is_empty(self):
        return len(self.stack) == 0

    def size(self):
        return len(self.stack)
    
def main():
    s = Stack()
    s.push(10)
    s.push(20)
    s.push(30)

    print("Top element:", s.peek())  
    print("Stack size:", s.size())   

    print("Popped:", s.pop())  
    print("Stack size:", s.size())   

    print("Is stack empty?", s.is_empty())  

if __name__=="__main__":
    main()