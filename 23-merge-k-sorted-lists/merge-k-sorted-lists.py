# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        minHeap = []
        
        for i,node in enumerate(lists):
            if node:
                heappush(minHeap, (node.val,i))

        dummy = ListNode()
        temp = dummy


        while minHeap:
            val,index = heappop(minHeap)
            temp.next = ListNode(val)
            temp = temp.next
            lists[index] = lists[index].next

            if lists[index]:
                heappush(minHeap, (lists[index].val,index))
        
        return dummy.next