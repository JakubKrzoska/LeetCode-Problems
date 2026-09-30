# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = slow.next
        while True:
            if not fast or not fast.next:
                return False
            if fast == slow:
                return True
            fast = fast.next.next
            slow = slow.next