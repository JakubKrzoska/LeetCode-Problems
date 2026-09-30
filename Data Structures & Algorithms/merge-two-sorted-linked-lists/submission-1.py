# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        start = dummy
        head1, head2 = list1, list2
        while head1 and head2:
            if head1.val <= head2.val:
                dummy.next = head1
                dummy = head1
                head1 = head1.next
            else:
                dummy.next = head2
                dummy = head2
                head2 = head2.next

        if head1:
            dummy.next = head1
        if head2:
            dummy.next = head2

        return start.next



