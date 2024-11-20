# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:


        total_count = 0
        temp = head
        while(temp is not None):
            total_count+=1
            temp = temp.next

        count = total_count -n -1
        if (count == -1):
            return head.next

        temp = head
        while (temp and count!=0):
            count = count-1
            temp = temp.next

        temp.next = temp.next.next

        return head
        