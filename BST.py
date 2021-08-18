#Binary Search Trees are a non-linear data structure.
#They consist of a root node and zero, one or two children where the children can again have 0,1, or 2 nodes as their children and so on
#In most cases, the time complexity of operations on a BST, which include, lookups, insertions and deletions, take O(log N) time
#Except for the worst case, where the tree is heavily unbalanced with all the nodes being on one side of the tree.
#In that case, it basically becomes a linked list and the time complexities go up to O(n)

#Lets implement an unbalanced Binary Search Tree first
#We will need a node class to store information about each node
#It will store the value(data) and the pointers to its left and right children

class Node():
    def __init__(self, val, left = None, right = None):
        self.val = val
        self.left =left
        self.right = right

# Empty BST with no root or children
class BST():
    def __init__(self):
        self.root = None
        self.number_of_nodes = 0
    # Inserts the new node into the BST
    # Time Complexity: O(log N)
    def insert(self, val):
        new_node = Node(val)
        # Check if the tree is empty, then we make the root node the new_node.
        if self.root == None:
            self.root = new_node
            self.number_of_nodes = 1
        # Else, we create a temporary pointer which points to the root node at first.
        else:
            current_node = self.root # <-- Temp node
            # Doesn't iterate through every single node.
            # It iterates using Divide & Conquer
            while(current_node.left != new_node) and (current_node.right != new_node):
                # If the new_node value is less than current_node value
                # Then go Left
                if new_node.val < current_node.val:
                    # If there's no element in current_node.left
                    # Then assign the current_node.left to the new_node
                    if current_node.left == None:
                        current_node.left = new_node
                    # If there's is an element in current_node.left
                    # Then change the current_node to become its left node
                    # Redo the loop until it hits a node that has nothing in current_node.left
                    # Which makes it go back to the if statement
                    else:
                        current_node = current_node.left
                # If the new_node value is greater than current_node value
                # Then go Right
                elif new_node.val > current_node.val:
                    # If there's no element in current_node.right
                    # Then assign the current_node.right to the new_node
                    if current_node.right == None:
                        current_node.right = new_node 
                    # If there's is an element in current_node.right
                    # Then change the current_node to be its right node
                    # Redo the loop until it hits a node that has nothing in current_node.right
                    # Which makes it go back to the if statement
                    else:
                        current_node = current_node.right
                # If the new_node value is the same as the current_node value
                # It means its a duplicate node so it will print an appropriate message  
                elif new_node.val == current_node.val:
                    print("\nNo duplicate vertex allowed!")
                    return
            self.number_of_nodes += 1

    # Looks through the BST to see if that value exists in the tree
    # Time Complexity: O(log N)
    def lookup(self,val):
        # Check if there is a root node exists. No root means no tree
        if self.root == None:
            return "Tree Is Empty"
        # If there is a root node run the following code ⬇
        else:
            current_node = self.root # <-- Temp node
            # While loop will stop when there is no node to go through.
            # because once its gone through the BST and its None 
            # it means we didn't find the node in the BST
            # Doesn't iterate through every single node.
            # It iterates using Divide & Conquer
            while current_node is not None:
                if val < current_node.val:
                    current_node = current_node.left
                elif val > current_node.val:
                    current_node = current_node.right
                elif current_node.val == val:
                    return "Found:", current_node.val
            return "Not Found"


my_bst = BST()

print(my_bst.lookup(9))
# Tree Is Empty

print()

my_bst.insert(9)
my_bst.insert(4)
my_bst.insert(6)
my_bst.insert(20)
my_bst.insert(170)
my_bst.insert(15)
my_bst.insert(1)

# The Tree we just built ^
#       9
#     /   \
#   4      20
# /   \   /   \       
# 1   6  15   170

print("Root:",my_bst.root.val)
print("Right of Root:",my_bst.root.right.val)
print("Left of Root",my_bst.root.left.val)
print("Right of 20:",my_bst.root.right.right.val)
print("Left of 20:",my_bst.root.right.left.val)
print("Right of 4:",my_bst.root.left.right.val)
print("Left of 4:",my_bst.root.left.left.val)
print("\nNumber of Nodes:",my_bst.number_of_nodes)

my_bst.insert(9)
# No duplicate vertex allowed!

print()

print(my_bst.lookup(9))
# ('Found:', 9)

print(my_bst.lookup(170))
# ('Found:', 170)

print(my_bst.lookup(666))
# Not Found