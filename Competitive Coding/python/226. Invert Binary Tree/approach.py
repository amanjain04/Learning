# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def invert(root):
            if (root is None):
                return
            tempa = root.left
            root.left = root.right
            root.right = tempa

            if (root.left):
                invert(root.left)
            if (root.right):
                invert(root.right)
            return root

        return invert(root)
        