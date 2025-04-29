class Stack:
    def __init__(self):
        self.stack = []
    
    def is_empty(self):
        return len(self.stack) == 0
    
    def push(self, e):
        self.stack.append(e)
        return self.stack
    
    def pop(self):
        if self.is_empty():
            return None
        item = self.stack.pop()
        return item
    
    def top(self):
        if self.is_empty():
            return None
        return self.stack[-1]
        
    def printStack(self):
        if self.is_empty():
            print("Stack is empty")
            return
        for item in reversed(self.stack):
            print(item, end=" , ")
        print()
    
if __name__ == "__main__":
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.printStack() # Output: 3 , 2 , 1 ,
    print(stack.top())  # Output: 3
    print(stack.pop())  # Output: 3
    print(stack.is_empty())  # Output: False
    stack.pop()
    stack.pop()
    print(stack.is_empty())  # Output: True
    print(stack.pop())  # Output: None