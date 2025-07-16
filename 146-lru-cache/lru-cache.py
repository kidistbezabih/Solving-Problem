class Linkedlist:
    def __init__(self, key, val):
        self.value = val
        self.key = key
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.memo = {}
        self.capacity = capacity

        self.head = Linkedlist(0, 0) 
        self.tail = Linkedlist(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head


    def get(self, key: int) -> int:
        if not key in self.memo:
            return -1
        
        self.remove(self.memo[key])
        self.insert_last(self.memo[key])

        return self.memo[key].value     

    def put(self, key: int, value: int) -> None:
        if key in self.memo:
            self.memo[key].value = value
            self.remove(self.memo[key])

        else:
            if self.capacity == 0:
                node_to_delete = self.head.next.key
                self.remove(self.memo[node_to_delete])
                del self.memo[node_to_delete]
                
            else:
                self.capacity -= 1
            self.memo[key] = Linkedlist(key, value)
        self.insert_last(self.memo[key])

    def remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    
    def insert_last(self, node):
        last_node = self.tail.prev  
        last_node.next = node
        node.prev = last_node
        node.next = self.tail
        self.tail.prev = node


    


            

'''
capacity = 2
dic = {
    1:1,
    2:2,
    3:3,
}
order = {1:1,
2:2,
3:3,
}

queue = [1,2,3]

'''     


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)