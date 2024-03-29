class Node:
    def __init__(self, data, color="red"):
        self.data = data  # The value or data contained in the node
        self.color = color  # The color of the node, default is "red"
        self.parent = None  # Reference to the parent node
        self.left = None  # Reference to the left child node
        self.right = None  # Reference to the right child node

class RedBlackTree:
    def __init__(self):
        self.NIL = Node(data=0, color="black")  # Sentinel NIL node
        self.root = self.NIL  # The root of the RBT initialized to the NIL node

def insert(self, data):
    new_node = Node(data)  # Create a new node with the given data
    new_node.left = self.NIL  # Set the new node's left child to NIL
    new_node.right = self.NIL  # Set the new node's right child to NIL

    parent = None  # Initialize parent node as None
    current = self.root  # Start traversal from the root

    # Find the correct position for the new node
    while current != self.NIL:
        parent = current
        if new_node.data < current.data:
            current = current.left
        else:
            current = current.right

    # Set the new node's parent
    new_node.parent = parent

    # Insert the new node in the appropriate position
    if parent is None:
        self.root = new_node
    elif new_node.data < parent.data:
        parent.left = new_node
    else:
        parent.right = new_node

    # Initially set the new node's color to red
    new_node.color = "red"
    self.fix_insert(new_node)  # Adjust the tree to maintain RBT properties

def fix_insert(self, node):
    # Fix the tree so that Red Black Tree properties are preserved
    while node != self.root and node.parent.color == 'red':
        if node.parent == node.parent.parent.left:
            uncle = node.parent.parent.right
            # Case 1: The uncle of node is red
            if uncle.color == 'red':
                node.parent.color = 'black'
                uncle.color = 'black'
                node.parent.parent.color = 'red'
                node = node.parent.parent
            else:
                # Case 2: Node is the right child of its parent
                if node == node.parent.right:
                    node = node.parent
                    self.leftRotate(node)
                # Case 3: Node is the left child of its parent
                node.parent.color = 'black'
                node.parent.parent.color = 'red'
                self.rightRotate(node.parent.parent)
        else:
            # Symmetric to the above condition
            uncle = node.parent.parent.left
            if uncle.color == 'red':
                node.parent.color = 'black'
                uncle.color = 'black'
                node.parent.parent.color = 'red'
                node = node.parent.parent
            else:
                if node == node.parent.left:
                    node = node.parent
                    self.rightRotate(node)
                node.parent.color = 'black'
                node.parent.parent.color = 'red'
                self.leftRotate(node.parent.parent)

    self.root.color = 'black'

def leftRotate(self, x):
    y = x.right
    x.right = y.left
    if y.left != self.NIL:
        y.left.parent = x
    y.parent = x.parent
    if x.parent is None:
        self.root = y
    elif x == x.parent.left:
        x.parent.left = y
    else:
        x.parent.right = y
    y.left = x
    x.parent = y

def rightRotate(self, x):
    y = x.left
    x.left = y.right
    if y.right != self.NIL:
        y.right.parent = x
    y.parent = x.parent
    if x.parent is None:
        self.root = y
    elif x == x.parent.right:
        x.parent.right = y
    else:
        x.parent.left = y
    y.right = x
    x.parent = y

