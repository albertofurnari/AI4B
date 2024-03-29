# Class definition for a tree node in an AVL Tree
class TreeNode:
    def __init__(self, key):
        self.key = key  # The value or key of the node
        self.left = None  # Pointer to the left child
        self.right = None  # Pointer to the right child
        self.height = 1  # The height of the node in the tree

# AVL Tree implementation
class AVLTree:
    # Function to insert a new key in the AVL tree
    def insert(self, root, key):
        # If the current node is None, create a new node with the key
        if not root:
            return TreeNode(key)
        elif key < root.key:
            # If the key is less than the current node's key, insert it into the left subtree
            root.left = self.insert(root.left, key)
        else:
            # If the key is greater than the current node's key, insert it into the right subtree
            root.right = self.insert(root.right, key)

        # Update the height of the ancestor node
        root.height = 1 + max(self.getHeight(root.left),
                              self.getHeight(root.right))

        # Get the balance factor to check whether this node became unbalanced
        balanceFactor = self.getBalance(root)

        # If the node is unbalanced, then there are 4 cases

        # Left Left Case
        if balanceFactor > 1 and key < root.left.key:
            return self.rightRotate(root)

        # Right Right Case
        if balanceFactor < -1 and key > root.right.key:
            return self.leftRotate(root)

        # Left Right Case
        if balanceFactor > 1 and key > root.left.key:
            root.left = self.leftRotate(root.left)
            return self.rightRotate(root)

        # Right Left Case
        if balanceFactor < -1 and key < root.right.key:
            root.right = self.rightRotate(root.right)
            return self.leftRotate(root)

        # Return the (possibly updated) root pointer
        return root

    # Helper function to get the height of the node
    def getHeight(self, root):
        if not root:
            return 0
        return root.height

    # Function to get the balance factor of the node
    def getBalance(self, root):
        if not root:
            return 0
        return self.getHeight(root.left) - self.getHeight(root.right)

    # Function to perform a left rotation on the subtree rooted with z
    def leftRotate(self, z):
        y = z.right
        T2 = y.left

        # Perform rotation
        y.left = z
        z.right = T2

        # Update heights
        z.height = 1 + max(self.getHeight(z.left),
                           self.getHeight(z.right))
        y.height = 1 + max(self.getHeight(y.left),
                           self.getHeight(y.right))

        # Return the new root
        return y

    # Function to perform a right rotation on the subtree rooted with y
    def rightRotate(self, y):
        x = y.left
        T2 = x.right

        # Perform rotation
        x.right = y
        y.left = T2

        # Update heights
        y.height = 1 + max(self.getHeight(y.left),
                           self.getHeight(y.right))
        x.height = 1 + max(self.getHeight(x.left),
                           self.getHeight(x.right))

        # Return the new root
        return x

# Example Usage
avl = AVLTree()  # Create an instance of AVLTree
root = None  # Start with an empty tree

# Sequentially insert keys into the AVL tree
root = avl.insert(root, 10)
root = avl.insert(root, 20)
root = avl.insert(root, 30)
root = avl.insert(root, 40)
root = avl.insert(root, 50)
root = avl.insert(root, 25)
