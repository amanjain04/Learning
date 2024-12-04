# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.count = 0
        def good(root,maxa):
            if root is None:
                return 
            if (root.val >= maxa):
                self.count+=1
                maxa = root.val
            good(root.left,maxa)
            good(root.right,maxa)
        good(root,float('-inf'))
        return self.count
        