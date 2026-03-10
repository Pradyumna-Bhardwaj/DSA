class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def preOrderTraversal(node):
    if node is None:
        return
    print(node.val, end=", ")
    preOrderTraversal(node.left)
    preOrderTraversal(node.right)

root = TreeNode(5)
nodeA = TreeNode(2)
nodeB = TreeNode(7)
nodeC = TreeNode(1)
# nodeD = TreeNode(4)
nodeE = TreeNode(6)
nodeF = TreeNode(8)
# nodeG = TreeNode(12)

root.left = nodeA
root.right = nodeB

# nodeA.left = nodeC
# nodeA.right = nodeD

nodeB.left = nodeE
nodeB.right = nodeF

# nodeF.left = nodeG

# Traverse
# preOrderTraversal(root)
# BST = True

def validate(node, low, high):
    if not node:
        return True
    if not (low < node.val < high):
        return False
    return (validate(node.left, low, node.val) and
            validate(node.right, node.val, high))

print(validate(root, float('-inf'), float('inf')))
