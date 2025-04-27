class AVLNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.ht = 1

class AVLTree:
    def ht(self, node):
        return node.ht if node else 0

    def bal(self, node):
        return self.ht(node.left) - self.ht(node.right) if node else 0

    def update_ht(self, node):
        node.ht = 1 + max(self.ht(node.left), self.ht(node.right))

    def r_rot(self, y):
        x = y.left
        T2 = x.right
        x.right = y
        y.left = T2
        self.update_ht(y)
        self.update_ht(x)
        return x

    def l_rot(self, x):
        y = x.right
        T2 = y.left
        y.left = x
        x.right = T2
        self.update_ht(x)
        self.update_ht(y)
        return y

    def insert(self, root, val):
        if not root:
            return AVLNode(val)

        if val < root.val:
            root.left = self.insert(root.left, val)
        elif val > root.val:
            root.right = self.insert(root.right, val)
        else:
            return root

        self.update_ht(root)
        b = self.bal(root)

        if b > 1:
            if val < root.left.val:
                return self.r_rot(root)
            else:
                root.left = self.l_rot(root.left)
                return self.r_rot(root)
        if b < -1:
            if val > root.right.val:
                return self.l_rot(root)
            else:
                root.right = self.r_rot(root.right)
                return self.l_rot(root)

        return root

    def search(self, root, val):
        if not root or root.val == val:
            return root
        return self.search(root.left, val) if val < root.val else self.search(root.right, val)

# Example usage (optional, remove if not needed for assignment)
avl = AVLTree()
root = None
for val in [10, 20, 30, 40, 50, 25]:
    root = avl.insert(root, val)
print("Search 25:", "Found" if avl.search(root, 25) else "Not Found")  # Found
print("Search 15:", "Found" if avl.search(root, 15) else "Not Found")  # Not Found