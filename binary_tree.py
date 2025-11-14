class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.key = key

def inorder(root):
    if root:
        inorder(root.left)
        print(root.key)
        inorder(root.right)

if __name__ == "__main__":
    root = Node(10)
    root.left = Node(5)
    root.right = Node(15)
    inorder(root)
