# Python program to find sum and product of 

# maximum and minimum in a Binary search Tree

 

_MIN=-2147483648 

_MAX=2147483648 

 

# Helper function that allocates a new 

# node with the given data and None left 

# and right pointers.                                 

class newNode: 

 

    # Constructor to create a new node 

    def init(self,data): 

        self.data = data 

        self.left = None 

        self.right = None 

 

# Function to insert a node in BST

def insert(node, data): 

 

    # 1. If the tree is empty, return a new,     

    # single node 

    if (node == None): 

        return (newNode(data)) 

    else: 

         

        # 2. Otherwise, recur down the tree 

        if (data <= node.data): 

            node.left = insert(node.left, data) 

        else: 

            node.right = insert(node.right, data) 

 

        # return the (unchanged) node pointer 

        return node 

     

 

 

# Function to find the node with maximum value

def maxValue(node): 

    current = node 

     

    # Find the rightmost leaf 

    while (current.right != None) : 

        current = current.right 

     

    return (current.data) 

 

 

# Function to find the node with minimum value

def minValue(node): 

 

    current = node 

 

    # Find the leftmost leaf 

    while (current.left != None): 

        current = current.left 

     

    return (current.data) 

 

 

         

# Driver Code 

if name == 'main': 

     

    # Create binary Tree 

    root = newNode(2) 

    insert(root, 1) 

    insert(root, 3) 

    insert(root, 6) 

    insert(root, 5) 

    max = maxValue(root) 

    min = minValue(root) 

     

    print("Sum of Maximum and Minimum" + 

            "element is ", max + min) 

    print("Product of Maximum and Minimum" + 

            "element is", max * min) 

     

# This code is contributed

# Shubham Singh(SHUBHAMSINGH10)
