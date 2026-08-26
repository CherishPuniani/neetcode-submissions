# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # abs(H of left - h of right) <= 1
        if not root:
            return True
        ans = True

        def get_depth(node: Optional[TreeNode]) -> int:
            nonlocal ans
            if not node:
                return 0

            left_depth = get_depth(node.left)
            right_depth = get_depth(node.right)

            if abs(left_depth - right_depth) > 1:
                ans = False

            # Return height to parent
            return 1 + max(left_depth, right_depth)
        
        get_depth(root)
        return ans
