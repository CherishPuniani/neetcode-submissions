#  this is optimised version of solution 1
class Solution:

  def isValidBST(self, root: Optional[TreeNode]) -> bool:
    prev = float("-inf")

    def dfs(node: Optional[TreeNode]) -> bool:
      nonlocal prev
      if not node:
        return True

      # 1. Check left subtree
      if not dfs(node.left):
        return False

      # 2. Check current node against previous visited value
      if node.val <= prev:
        return False
      prev = node.val

      # 3. Check right subtree
      return dfs(node.right)

    return dfs(root)