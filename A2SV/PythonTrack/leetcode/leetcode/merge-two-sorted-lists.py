# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1 and not list2:
            return None

        head1 = list1
        head2 = list2
        prev = None

        while head1 or head2:
            if head1 and head2:
                if min(head1.val, head2.val) == head1.val:
                    if prev:
                        prev.next = head1
                    else:
                        head = head1
                    prev = head1
                    head1 = head1.next
                else:
                    if prev:
                        prev.next = head2
                    else:
                        head = head2
                    prev = head2
                    head2 = head2.next
            else:
                if head1:
                    if prev:
                        prev.next = head1
                    else:
                        head = head1
                    prev = head1
                    head1 = head1.next
                else:
                    if prev:
                        prev.next = head2
                    else:
                        head = head2
                    prev = head2
                    head2 = head2.next
        return head