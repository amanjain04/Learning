# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if (head is None or head.next is None):
            return head

        temp = ListNode(0)

        node = temp

        while (head and head.next):
            first = head
            second = head.next
            node.next = second
            nexx = second.next
            second.next = first
            first.next = nexx
            head = nexx
            node =first

        return temp.next