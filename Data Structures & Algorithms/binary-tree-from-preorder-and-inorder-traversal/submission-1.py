class Solution:

  def buildTree(
      self, preorder: List[int], inorder: List[int]
  ) -> Optional[TreeNode]:
    in_map = {val: i for i, val in enumerate(inorder)}
    pre_idx = 0

    def helper(in_start: int, in_end: int) -> Optional[TreeNode]:
      nonlocal pre_idx
      if in_start > in_end:
        return None

      root_val = preorder[pre_idx]
      pre_idx += 1

      root = TreeNode(root_val)
      mid = in_map[root_val]

      root.left = helper(in_start, mid - 1)
      root.right = helper(mid + 1, in_end)
      return root

    return helper(0, len(inorder) - 1)