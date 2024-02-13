# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return None

        length  = 0
        last = head 
        ahead = head
        while last:
            length  += 1
            ahead = last
            last = last.next

        k %= length
        if k == 0 or  k == length:
            return head

        current = head
        for i in range(length-k-1):
            current = current.next
            
        nx = current.next
        current.next = None
        ahead.next = head
        head = nx
        return nx


      
