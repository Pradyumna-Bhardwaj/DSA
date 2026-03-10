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

root = TreeNode('R')
nodeA = TreeNode('A')
nodeB = TreeNode('B')
nodeC = TreeNode('C')
nodeD = TreeNode('D')
nodeE = TreeNode('E')
nodeF = TreeNode('F')
nodeG = TreeNode('G')

root.left = nodeA
root.right = nodeB

nodeA.left = nodeC
nodeA.right = nodeD

nodeB.left = nodeE
nodeB.right = nodeF

nodeF.left = nodeG

from collections import deque
def lateralT(root):
    Q = deque([root])
    result = []
    while Q:
        level = []
        lenQ = len(Q)
        for i in range(lenQ):
            node = Q.popleft()
            level.append(node.val)
            if node.left:
                Q.append(node.left)
            if node.right:
                Q.append(node.right)
        result.append(level)
    print(result)