# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution: # GPT's Code as well
    def minDepth(self, root: Optional[TreeNode]) -> int:
        # base case
        if not root:
            return 0

        # if one of the children is missing, we cannot take min() directly
        if not root.left and not root.right:
            return 1

        if not root.left:
            return 1 + self.minDepth(root.right)
        if not root.right:
            return 1 + self.minDepth(root.left)

        # both children exist
        return 1 + min(self.minDepth(root.left), self.minDepth(root.right))
        
        
