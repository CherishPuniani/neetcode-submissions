# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        count = 0 # If there is a node then atleast 1 good node

        def dfs(node, maxC):
            nonlocal count
            if not node:
                return
            if node.val >= maxC:
                count += 1
                maxC = node.val
            
            dfs(node.left, maxC)
            dfs(node.right, maxC)

        dfs(root, root.val)
        return count
