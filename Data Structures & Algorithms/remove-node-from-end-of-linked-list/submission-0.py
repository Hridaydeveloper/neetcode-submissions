# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr = head
        prev = None

        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node

        count = 1
        curr = prev
        if n == 1:
            prev = prev.next
        else:

            while curr:
                if count + 1 == n:
                    curr.next = curr.next.next
                curr = curr.next
                count += 1


        res = None
        curr = prev
        while curr:
            next_node = curr.next
            curr.next = res
            res = curr
            curr = next_node

        return res
