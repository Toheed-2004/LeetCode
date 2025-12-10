class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def is_mirror(left, right):
            if not left and not right:
                return True
            if not left or not right:
                return False
            if left.val != right.val:
                return False
            # recursive mirror check
            return is_mirror(left.left, right.right) and is_mirror(left.right, right.left)

        if not root:
            return True
        return is_mirror(root.left, root.right)