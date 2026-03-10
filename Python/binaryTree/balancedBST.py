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
def inOrderTraversal(node):
    if node is None:
        return
    inOrderTraversal(node.left)
    print(node.val, end=", ")
    inOrderTraversal(node.right)

from lateralTraversal import lateralT

nums = [-10,-3,0,5,9]

# root = TreeNode(nums[int(len(nums)/2)])

def addNode(arr):
    if not arr:
        return None

    mid = len(arr)//2

    node = TreeNode(arr[mid])

    node.left = addNode(arr[:mid])
    node.right = addNode(arr[mid+1:])

    return node
root = addNode(nums)

print(root.val)


