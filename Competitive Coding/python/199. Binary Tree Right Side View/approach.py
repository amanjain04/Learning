# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if (root is None):
            return []
        queue = deque([root])

        ans = []

        while (queue):
            length = len(queue)
            temp = []
            for i in range(length):
                parent =  queue.popleft()
                temp.append(parent.val)
                if (parent.left):
                    queue.append(parent.left)
                if (parent.right):
                    queue.append(parent.right)
                
            ans.append(temp)

        for i in range(len(ans)):
            ans[i] = ans[i][-1]
        return ans
        