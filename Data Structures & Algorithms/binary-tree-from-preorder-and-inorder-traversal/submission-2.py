# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        hmapp = {val:i for i, val in enumerate(inorder)}
        pre_idx = 0

        def solve(idx_s, idx_e):
            nonlocal pre_idx
            # What would be the base condition?
            if idx_e < idx_s:
                return None
            root = TreeNode(preorder[pre_idx])
            mid = hmapp[preorder[pre_idx]]
            pre_idx += 1

            root.left = solve(idx_s, mid-1)
            root.right = solve(mid+1,idx_e)
            return root

        return solve(0, len(preorder)-1)

        # return TreeNode(preorder[0])