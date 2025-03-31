class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.top = None  # Head of the stack
    
    # Push element to the top - O(1)
    def push(self, x):
        new_node = Node(x)
        new_node.next = self.top
        self.top = new_node
    
    # Pop element from the top - O(1)
    def pop(self):
        if self.top is None:  # If stack is empty
            return None
        popped = self.top.data
        self.top = self.top.next
        return popped
    
    # Get top element without removing - O(1)
    def peek(self):
        if self.top is None:
            return None
        return self.top.data
    
    # Check if stack is empty - O(1)
    def is_empty(self):
        return self.top is None
    
    # Helper function to print stack (for testing)
    def print_stack(self):
        current = self.top
        if current is None:
            print("Stack is empty")
            return
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("Bottom")

# Example usage
if __name__ == "__main__":
    s = Stack()
    print("Is empty?", s.is_empty())  # True
    
    s.push(1)  # 1
    s.push(2)  # 2 -> 1
    s.push(3)  # 3 -> 2 -> 1
    s.print_stack()  # 3 -> 2 -> 1 -> Bottom
    
    print("Top element:", s.peek())  # 3
    print("Popped:", s.pop())        # 3, stack: 2 -> 1
    s.print_stack()  # 2 -> 1 -> Bottom
    
    print("Popped:", s.pop())        # 2, stack: 1
    print("Popped:", s.pop())        # 1, stack: empty
    print("Is empty?", s.is_empty()) # True