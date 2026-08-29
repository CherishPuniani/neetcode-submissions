class Solution:

  def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
    if not root:
      return []
    ans, q = [], deque([root])
    while q:
      ans.append(q[-1].val)
      for _ in range(len(q)):
        node = q.popleft()
        if node.left:
          q.append(node.left)
        if node.right:
          q.append(node.right)
    return ans