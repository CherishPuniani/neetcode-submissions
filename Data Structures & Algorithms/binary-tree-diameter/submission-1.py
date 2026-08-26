# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=, Self0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def calcDepth(self, root: Optional[TreeNode]):
        if not root:
            return 0

        return max(self.calcDepth(root.left), self.calcDepth(root.right)) + 1
        
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        maxDia = 0
        dia = self.calcDepth(root.left) + self.calcDepth(root.right)
    
        return max(self.diameterOfBinaryTree(root.left),self.diameterOfBinaryTree(root.right),dia)
