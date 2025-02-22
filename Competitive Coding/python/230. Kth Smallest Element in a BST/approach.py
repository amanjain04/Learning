# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.result = []
        def inor(root):
            if (root is None):
               return None
            inor(root.left)
            self.result.append(root.val)
            inor(root.right)
            return
        inor(root)
        return self.result[k-1]
        