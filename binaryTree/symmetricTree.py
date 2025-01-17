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

root = TreeNode(1)
nodeA = TreeNode(2)
nodeB = TreeNode(2)
nodeC = TreeNode(3)
nodeD = TreeNode(4)
nodeE = TreeNode(4)
nodeF = TreeNode(3)
# nodeG = TreeNode('G')

root.left = nodeA
root.right = nodeB

nodeA.left = nodeC
nodeA.right = nodeD

nodeB.left = nodeE
nodeB.right = nodeF

# nodeF.left = nodeG


nodeR = root
nodeL = root

arrR = []
arrL = []

# while(nodeR is not None and nodeL is not None):
#     arrR.append(nodeR.val)
#     arrL.append(nodeL.val)

def inorderTraversalLeft(root):
  
    # Base case: if null
    if root is None:
        arrL.append("A")
        return
      
    # Recur on the left subtree
    inorderTraversalLeft(root.left)
    
    # Recur on the right subtree
    inorderTraversalLeft(root.right)
    # Visit the current node
    arrL.append(root.val)

def inorderTraversalRight(root):
  
    # Base case: if null
    if root is None:
        arrR.append("A")
        return
      
    # Recur on the left subtree
    inorderTraversalRight(root.right)
    
    # Recur on the right subtree
    inorderTraversalRight(root.left)
    # Visit the current node
    arrR.append(root.val)

inorderTraversalLeft(root)
inorderTraversalRight(root)

# if (len(arrR) == len(arrL)):
#     for i in range(len(arrL)):
#         if(arrL[i]!=arrR[i]):
#             print(False)
# else:
#     print(False)

print(arrL)
print(arrR)
    