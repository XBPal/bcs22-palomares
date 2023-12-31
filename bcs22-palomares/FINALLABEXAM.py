# creates a class that denotes each node of the tree
class Node:

    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

# defines left to right vertical traversal function
def VOrder_LR(root, column, n):
    # checks for roots
    if root is None:
        return

    # appends nodes
    try:
        n[column].append(root.key)
    except:
        n[column] = [root.key]

    # recursively calls function for left and right nodes
    # if node is on the left, subtract one to horizontal distance
    # if node is on the right, adds one to its horizontal distance
    VOrder_LR(root.left, column - 1, n)
    VOrder_LR(root.right, column + 1, n)

# defines right to left vertical traversal function
def VOrder_RL(root, column, n):
    if root is None:
        return
    try:

        n[column].append(root.key)
    except:
        n[column] = [root.key]

    # recursively calls function for left and right nodes
    # if node is on the left, adds one to its horizontal distance
    # if node is on the right, subtracts one to its horizontal distance
    VOrder_RL(root.right, column - 1, n)
    VOrder_RL(root.left, column + 1, n)

# reverses the order of the functions
def printreverseRL(root):
    rn = {}
    rrn = []
    column = 0
    VOrder_LR(root, column, rn)

    print("Output:")
    for index, value in enumerate(sorted(rn)):
        for i in rn[value]:
            rrn.append(i)

    print(str(rrn[::-1]))

# defines a function that prints the reversed right to left function.
def printing(root):
    printreverseRL(root)

# defines the main tree
def main():
    # defines the nodes
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)
    root.right.left.right = Node(8)
    root.right.right.right = Node(9)

    printing(root)

# calls main function
main()