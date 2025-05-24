class Node:
    def __init__(self, key=None, value=None):
        self.value = value
        self.key = key
        self.next = None 
        self.prev = None

class LRUCache:
    def __init__(self, capacity: int):
        self.cache = {}
        self.capacity = capacity

        self.lru = Node()
        self.mru = Node()
        self.lru.next = self.mru
        self.mru.prev = self.lru

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            self.remove(node)
            self.add(node)
            return node.value
        return -1
            
    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        
        node = Node(key, value)
        self.cache[key] = node

        if len(self.cache) > self.capacity:
            l = self.lru.next
            self.remove(l)
            del self.cache[l.key]

        self.add(node)
        self.cache[key] = node

    def add(self, node:Node) -> None:
        prev = self.mru.prev
        prev.next = node
        node.prev = prev
        node.next = self.mru
        self.mru.prev = node

    def remove(self, node: Node) -> None:
        node.prev.next = node.next
        node.next.prev = node.prev

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)