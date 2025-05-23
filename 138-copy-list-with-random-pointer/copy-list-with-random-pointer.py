"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        copy = {}
        temp = head

        while temp:
            copy[temp] = Node(temp.val)
            temp = temp.next
        ans = None

        for old_node, new_node in copy.items():
            if not ans:
                ans = new_node
            new_node.next = copy[old_node.next] if old_node.next in copy else None
            new_node.random = copy[old_node.random] if old_node.random in copy else None

        return ans