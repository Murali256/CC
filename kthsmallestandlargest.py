# A simple inorder traversal based Python3
# program to find k-th smallest element
# in a BST.

# A BST node
class Node:
	
	def __init__(self, key):
		
		self.data = key
		self.left = None
		self.right = None

# Recursive function to insert an key into BST
def insert(root, x):
	
	if (root == None):
		return Node(x)
	if (x < root.data):
		root.left = insert(root.left, x)
	elif (x > root.data):
		root.right = insert(root.right, x)
	return root

# Function to find k'th largest element
# in BST. Here count denotes the number
# of nodes processed so far
def kthSmallest(root):
	
	global k
	
	# Base case
	if (root == None):
		return None

	# Search in left subtree
	left = kthSmallest(root.left)

	# If k'th smallest is found in
	# left subtree, return it
	if (left != None):
		return left
		
	# If current element is k'th
	# smallest, return it
	k -= 1
	if (k == 0):
		return root

	# Else search in right subtree
	return kthSmallest(root.right)

# Function to find k'th largest element in BST
def printKthSmallest(root):
	
	# Maintain index to count number
	# of nodes processed so far
	count = 0
	res = kthSmallest(root)
	
	if (res == None):
		print("There are less than k nodes in the BST")
	else:
		print("K-th Smallest Element is ", res.data)
		
def kthLargest(root):
	
	global k
	
	# Base case
	if (root == None):
		return None

	# Search in left subtree
	right = kthLargest(root.right)

	# If k'th smallest is found in
	# left subtree, return it
	if (right != None):
		return right
		
	# If current element is k'th
	# smallest, return it
	k -= 1
	if (k == 0):
		return root

	# Else search in right subtree
	return kthLargest(root.left)

# Function to find k'th largest element in BST
def printKthLargest(root):
	
	# Maintain index to count number
	# of nodes processed so far
	count = 0
	res = kthLargest(root)
	
	if (res == None):
		print("There are less than k nodes in the BST")
	else:
		print("K-th Largest Element is ", res.data)



# Driver code
if __name__ == '__main__':
	
	root = None
	#keys = [ 20, 8, 22, 4, 12, 10, 14 ]
	keys = [ 15,10,20,8,12,16,25 ]


	for x in keys:
		root = insert(root, x)

	k = 2
	
	printKthSmallest(root)
	
	printKthLargest(root)

# This code is contributed by mohit kumar 29
