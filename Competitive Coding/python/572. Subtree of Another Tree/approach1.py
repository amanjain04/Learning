class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        string_root = self.traverse_tree(root)
        string_sub = self.traverse_tree(subRoot)
        if string_sub in string_root:
            return True
        return False
    
    def traverse_tree(self, node):
        if node:
            return f"#{node.val} {self.traverse_tree(node.left)} {self.traverse_tree(node.right)}"
        return 'n'