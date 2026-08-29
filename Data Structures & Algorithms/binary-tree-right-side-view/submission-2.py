# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root is None: return []
        ans = []
        def bfs( node ):
            q = deque( [node] )
            while q:
                ans.append( q[-1].val )
                for _ in range( len( q ) ):
                    u = q.popleft()
                    if u.left:  q.append( u.left )
                    if u.right: q.append( u.right )
        bfs(root)
        return ans