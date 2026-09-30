# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        tail = dummy

        head1 = list1
        head2 = list2

        while head1 and head2:
            if head1.val > head2.val:
                tail.next = head2
                tail = head2
                head2 = head2.next
            else:
                tail.next = head1
                tail = head1
                head1 = head1.next
        
        if head1:
            tail.next = head1
        if head2:
            tail.next = head2
        
        return dummy.next
    

        