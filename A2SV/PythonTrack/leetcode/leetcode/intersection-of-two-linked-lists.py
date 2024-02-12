# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        if not headA or not headB:
            return None
        s = set()

        while headA.next or headB.next:
            if headA in s:
                return headA
            if headA.next:
                s.add(headA)
                headA = headA.next

            if headB in s:
                return headB
            if headB.next:
                s.add(headB)
                headB = headB.next
        if headA == headB:
            return headA 
            
 
        