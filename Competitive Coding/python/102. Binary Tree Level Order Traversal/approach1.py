# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if (root is None):
            return []
        hashmpa = []
        def level_check(root, hashmpa, level):
            if (root is None):
                return root
            if (len(hashmpa) == level):
                hashmpa.append([root.val])
            else:
                hashmpa[level].append(root.val)
            level_check(root.left,hashmpa,level+1)
            level_check(root.right,hashmpa,level+1)
        level_check(root,hashmpa,0)
        return hashmpa




        
        