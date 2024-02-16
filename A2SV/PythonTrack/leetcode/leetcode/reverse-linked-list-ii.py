# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        prev = None
        left_node = None
        current = head
        index = 1

        while index != left:
            prev = current
            current = current.next
            index += 1

        left_node = current
        right_node = current.next
        while index < right:
            temp = current
            current = right_node
            index += 1
            right_node = current.next
            current.next = temp

        if prev :
            prev.next = current
        else:
            head = current
        left_node.next = right_node
        return head


        