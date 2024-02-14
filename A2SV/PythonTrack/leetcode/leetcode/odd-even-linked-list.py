class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head :
            return None
        even=None
        temp=head
        i=1

        if head.next and head.next.next:
            even = head.next
        else:
            return head
        
        while temp.next.next:
            curr=temp
            temp=temp.next
            curr.next=curr.next.next
            i+=1
        if i%2==0:
            end=temp.next
            temp.next=None
            end.next=even
        else:
            temp.next.next=None
            temp.next=even
        return head