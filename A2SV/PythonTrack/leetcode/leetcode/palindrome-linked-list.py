# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        s = copy.deepcopy(head)

        def reversed_linked_list(s):
            prev = None
            current = s

            while current:
                next_val = current.next
                current.next = prev
                prev = current
                current = next_val
            return prev

        reversed_list = reversed_linked_list(s)
        while reversed_list and head:
            if reversed_list.val != head.val:
                return False
            reversed_list = reversed_list.next
            head = head.next
        return True
        