# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        ans = []
        q1 = deque()
        q2 = deque()
        q1.append(root)
        while q1 or q2:
            if q1:
                temp_list = [node.val for node in q1]
                ans.append(temp_list)
                while q1:
                    node = q1.popleft()
                    if node.left:
                        q2.append(node.left)
                    if node.right:
                        q2.append(node.right)
            if q2:
                temp_list = [node.val for node in q2]
                ans.append(temp_list)
                while q2:
                    node = q2.popleft()
                    if node.left:
                        q1.append(node.left)
                    if node.right:
                        q1.append(node.right)
            # ans.append([node])

        return ans
            
