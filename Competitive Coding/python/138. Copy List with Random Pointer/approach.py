"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return head
        dict1 = {None:None}
        temp = head
        while(temp):
            newnode = Node(temp.val)
            dict1[temp]=newnode
            temp = temp.next
        temp =head
        while(temp):
            dict1[temp].next= dict1[temp.next]
            dict1[temp].random = dict1[temp.random]
            temp= temp.next
        return dict1[head]
        