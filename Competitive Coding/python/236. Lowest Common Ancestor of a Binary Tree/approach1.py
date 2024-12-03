# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        hashmap = {root:None}

        queue = deque([root])

        while(queue):
            parent = queue.popleft()
            if (parent.left):
                queue.append(parent.left)
                hashmap[parent.left] = parent
            if (parent.right):
                queue.append(parent.right)
                hashmap[parent.right] = parent

        def level(node_c):
            ans, nodec = 0, node_c
            while hashmap[nodec] != None:
                nodec = hashmap[nodec]
                ans+=1
            return ans
        
        a, b = level(p),level(q)

        if a>b:
            for _ in range(a-b):
                p = hashmap[p]
        if b>a:
            for _ in range(b-a):
                q = hashmap[q]

        while p!=q:
            p = hashmap[p]
            q = hashmap[q]
        return p