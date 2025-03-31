class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
    
    # i. Insert at beginning - O(1)
    def insert_beginning(self, x):
        new_node = Node(x)
        new_node.next = self.head
        self.head = new_node
    
    # ii. Insert at ith position - O(n)
    def insert_at(self, x, i):
        if i < 0:
            return
        new_node = Node(x)
        if i == 0:
            new_node.next = self.head
            self.head = new_node
            return
        current = self.head
        for _ in range(i - 1):
            if current is None:
                return
            current = current.next
        if current is None:
            return
        new_node.next = current.next
        current.next = new_node
    
    # iii. Remove from beginning - O(1)
    def remove_beginning(self):
        if self.head is None:
            return
        self.head = self.head.next
    
    # iv. Remove from ith position - O(n)
    def remove_at(self, i):
        if self.head is None or i < 0:
            return
        if i == 0:
            self.head = self.head.next
            return
        current = self.head
        for _ in range(i - 1):
            if current is None:
                return
            current = current.next
        if current is None or current.next is None:
            return
        current.next = current.next.next
    
    # v. Remove from end - O(n)
    def remove_end(self):
        if self.head is None:
            return
        if self.head.next is None:
            self.head = None
            return
        current = self.head
        while current.next.next:
            current = current.next
        current.next = None
    
    # vi. Search for element - O(n)
    def search(self, x):
        current = self.head
        while current:
            if current.data == x:
                return current
            current = current.next
        return None
    
    # vii. Insert at end - O(n)
    def insert_end(self, x):
        new_node = Node(x)
        if self.head is None:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    # Helper function to print list (for testing)
    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

# Example usage
if __name__ == "__main__":
    sll = SinglyLinkedList()
    sll.insert_beginning(1)  # 1
    sll.insert_end(3)        # 1 -> 3
    sll.insert_at(2, 1)      # 1 -> 2 -> 3
    sll.print_list()
    
    sll.remove_beginning()   # 2 -> 3
    sll.remove_at(1)         # 2
    sll.remove_end()         # empty
    sll.print_list()
    
    sll.insert_end(5)
    print(sll.search(5).data if sll.search(5) else "Not found")  # 5