class Node:
    def __init__(self,val=None):
        self.next = None
        self.val = val

class MyLinkedList:
    def __init__(self):
        self.head = None
        

    def get(self, index: int) -> int:
        temp = self.head
        while temp and index > 0:

            temp = temp.next
            index -= 1
        if temp and index == 0:
            return temp.val
        return(-1)

    def addAtHead(self, val: int) -> None:
        our_node = Node(val)
        temp = self.head
        if self.head:
            our_node.next = temp
            self.head = our_node
        else:
            self.head = our_node
        
    def addAtTail(self, val: int) -> None:
        our_node = Node(val)
        if self.head:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = our_node
        else:
            self.head= our_node
       
    def addAtIndex(self, index: int, val: int) -> None:
        our_node = Node(val)
        temp = self.head
        if index == 0:
            self.addAtHead(val)
        else:
            index-=1
            while index  > 0:
                if temp:
                    temp = temp.next
                index -= 1

            if index == 0 and temp:
                our_node.next = temp.next
                temp.next = our_node
        
    def deleteAtIndex(self, index: int) -> None:
        temp = self.head
        if index == 0:
            if self.head:
                self.head = self.head.next
        else:
            index-=1
            while index > 0:
                if temp:
                    temp = temp.next
                index -= 1
            if index == 0:
                if temp and temp.next:
                    temp.next = temp.next.next
                elif temp:
                    temp.next=None

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)