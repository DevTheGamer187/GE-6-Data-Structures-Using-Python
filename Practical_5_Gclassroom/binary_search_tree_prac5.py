class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    # i. Insert an element x
    def insert(self, x):
        self.root = self._insert(self.root, x)

    def _insert(self, node, x):
        if not node:
            return Node(x)
        if x < node.value:
            node.left = self._insert(node.left, x)
        else:
            node.right = self._insert(node.right, x)
        return node
    

    # ii. Delete an element x
    def delete(self, x):
        self.root = self._delete(self.root, x)

    def _delete(self, node, x):
        if not node:
            return None
        if x < node.value:
            node.left = self._delete(node.left, x)
        elif x > node.value:
            node.right = self._delete(node.right, x)
        else:
            # Node to delete found
            if not node.left:
                return node.right
            if not node.right:
                return node.left
            # Node has two children
            min_node = self._find_min(node.right)
            node.value = min_node.value
            node.right = self._delete(node.right, min_node.value)
        return node

    def _find_min(self, node):
        current = node
        while current.left:
            current = current.left
        return current
    
    # iii. Search for an element x
    def search(self, x):
        return self._search(self.root, x) is not None

    def _search(self, node, x):
        if not node or node.value == x:
            return node
        if x < node.value:
            return self._search(node.left, x)
        return self._search(node.right, x)
    
    # iv. Display traversals
    def preorder(self):
        result = []
        self._preorder(self.root, result)
        return result

    def _preorder(self, node, result):
        if node:
            result.append(node.value)
            self._preorder(node.left, result)
            self._preorder(node.right, result)

    def inorder(self):
        result = []
        self._inorder(self.root, result)
        return result

    def _inorder(self, node, result):
        if node:
            self._inorder(node.left, result)
            result.append(node.value)
            self._inorder(node.right, result)

    def postorder(self):
        result = []
        self._postorder(self.root, result)
        return result

    def _postorder(self, node, result):
        if node:
            self._postorder(node.left, result)
            self._postorder(node.right, result)
            result.append(node.value)

# Test the BST
if __name__ == "__main__":
    bst = BST()
    values = [5, 3, 7, 1, 4, 6, 8]
    for x in values:
        bst.insert(x)

    print("Preorder:", bst.preorder())    
    print("Inorder:", bst.inorder())      
    print("Postorder:", bst.postorder())  

    print("Search 4:", bst.search(4))     
    print("Search 9:", bst.search(9))     

    bst.delete(3)
    print("After deleting 3, Inorder:", bst.inorder())  