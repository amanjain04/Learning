# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        stack_a = [(root,1)]
        max_depth = 0
        while stack_a:
            node,depth = stack_a.pop()
            if node:
                max_depth = max(max_depth, depth)
                stack_a.append((node.left,depth+1))
                stack_a.append((node.right,depth+1))
        return max_depth
        