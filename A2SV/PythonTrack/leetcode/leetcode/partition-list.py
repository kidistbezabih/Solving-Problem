# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        if not head:
            return
        left = None
        right = None
        right_prev = None
        left_prev = None
        current = head
        right_head =  None

        while current:
            if current.val < x:
                left = current
                if not left_prev:
                    head = left
                else:
                    left_prev.next = left
                left_prev = left                 
            else:
                right = current
                if not right_prev:
                    right_head = right
                else:
                    right_prev.next = right
                right_prev = right

            current = current.next
        if left:
            left.next = right_head
        else:
            head = right_head
        if right:
            right.next = None
        return head
