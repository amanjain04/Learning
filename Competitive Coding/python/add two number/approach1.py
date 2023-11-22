# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        a = ListNode(0)
        b = a
        flag =0
        while(l1 and l2):
            temp = l1.val+l2.val +flag

            if (temp>9):
                flag = 1
            else:
                flag = 0
            temp = temp%10
            new_node = ListNode(temp)
            a.next = new_node
            a= a.next
            l1 = l1.next
            l2 = l2.next

        while(l1):
            temp = flag + l1.val
            if (temp>9):
                flag = 1
            else:
                flag = 0
            temp = temp%10
            new_node = ListNode(temp)
            a.next = new_node
            a= a.next
            l1 = l1.next

        while (l2):
            temp = flag + l2.val
            if (temp>9):
                flag = 1
            else:
                flag = 0
            temp = temp%10
            new_node = ListNode(temp)
            a.next = new_node
            a= a.next
            l2 = l2.next

        if flag > 0:
            new_node = ListNode(flag)
            a.next = new_node
            a= a.next


        return b.next

