# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head:
            fast = head
            slow = head
            index = 0

            while fast.next and fast.next.next:
                fast = fast.next.next
                slow = slow.next

                if fast == slow:
                    while slow != head:
                        slow = slow.next
                        head = head.next
                        index += 1
                    return head

