# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        trav = deque()
        trav.append(root)

        while trav:
            node = trav.popleft()
            temp = node.right
            node.right = node.left
            node.left = temp
            if node.left:
                trav.append(node.left)
            if node.right:
                trav.append(node.right)
        
        return root