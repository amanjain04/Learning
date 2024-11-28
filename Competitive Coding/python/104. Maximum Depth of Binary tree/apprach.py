# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        count = 0

        def depth(root, height):
            if (root is None):
                return height
            return max(depth(root.left,height+1),depth(root.right,height+1))
        return depth(root,0)
        