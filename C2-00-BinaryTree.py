# Definition for a binary tree node.
class TreeNode:
    # Constructor to create a new node
    def __init__(self, key):
        self.left = None  # Initialize left child to None
        self.right = None  # Initialize right child to None
        self.val = key  # Assign value to the node

# Function to insert a node into the binary search tree
def insert(root, key):
    # If the tree is empty, return a new node
    if root is None:
        return TreeNode(key)
    else:
        # Otherwise, recur down the tree
        if root.val < key:
            # If the given key is greater than the root's key, insert in right subtree
            root.right = insert(root.right, key)
        else:
            # If the given key is smaller than the root's key, insert in left subtree
            root.left = insert(root.left, key)
    # Return the (unchanged) node pointer
    return root

# Function to perform inorder traversal of the tree
def inorder_traversal(root):
    if root:
        # First recur on left child
        inorder_traversal(root.left)
        # Then print the data of the node
        print(root.val, end=' ')
        # Now recur on right child
        inorder_traversal(root.right)


# Example Usage

# Creating the root node of the tree with value 50
root = TreeNode(50)
# Inserting nodes into the tree
insert(root, 30)
insert(root, 20)
insert(root, 40)
insert(root, 70)
insert(root, 60)
insert(root, 80)

# Printing the inorder traversal of the binary tree
print("Inorder traversal of the binary tree:")
inorder_traversal(root)
