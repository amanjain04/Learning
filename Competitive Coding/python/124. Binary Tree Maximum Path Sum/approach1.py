# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        self.result =  float('-inf')

        def maxp(root):
            if not root:
                return 0
            left = max(0, maxp(root.left))
            right = max(0, maxp(root.right))
            current_sum_path = left + right + root.val
            self.result = max( self.result, current_sum_path)
            return (root.val + max(left , right))
        maxp(root)
        return self. result



        