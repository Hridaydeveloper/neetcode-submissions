# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        if l1 is None and l2 is None:
            return None

        carry = 0
        head = ListNode(0)
        curr = head

        while l1 or l2 or carry:
            if l1 is not None:
                num1 = l1.val
            else:
                num1 = 0

            if l2 is not None:
                num2 = l2.val
            else:
                num2 = 0

            ans = num1 + num2 + carry

            carry = ans // 10
            digit = ans % 10

            curr.next = ListNode(digit)
            curr = curr.next

            if l1:
                l1 = l1.next

            if l2:
                l2 = l2.next

        return head.next


        