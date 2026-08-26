class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        max_dia = 0

        def get_depth(node: Optional[TreeNode]) -> int:
            nonlocal max_dia
            if not node:
                return 0

            left_depth = get_depth(node.left)
            right_depth = get_depth(node.right)

            # Update max diameter found so far at the current node
            max_dia = max(max_dia, left_depth + right_depth)

            # Return height to parent
            return 1 + max(left_depth, right_depth)

        get_depth(root)
        return max_dia