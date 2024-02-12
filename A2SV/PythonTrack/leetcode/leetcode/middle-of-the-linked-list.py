# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp = head
        elements = 0
        while temp:
            elements +=1
            temp = temp.next

        half = elements//2  
        temp = head
        while temp and half > 0:
                temp = temp.next
                half -= 1

        return temp

        