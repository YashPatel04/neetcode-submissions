class Node:
    def __init__(self, key, val):
        self.key, self.value = key, val
        self.prev = self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.map = {}
        self.capacity = capacity
        self.size = 0
        self.left = Node(0, 0)
        self.right = Node(0, 0)
        self.left.next = self.right
        self.right.prev = self.left

    def addToFront(self, n: Node) -> None:
        nex = self.left.next
        nex.prev = n
        self.left.next = n
        n.next = nex
        n.prev = self.left

    def remove(self, n: Node) -> None:
        n.prev.next, n.next.prev = n.next, n.prev
        n = None

    def get(self, key: int) -> int:
        if key not in self.map:
            return -1
        n = self.map[key]
        self.remove(n)
        self.addToFront(n)
        return n.value

    def put(self, key: int, value: int) -> None:
        if key not in self.map:    
            n = Node(key, value)
            if (self.size+1)>self.capacity:
                del self.map[self.right.prev.key]
                self.remove(self.right.prev)
            else:
                self.size+=1
            self.map[key] = n
            self.addToFront(n)
        else:
            n = self.map[key]
            n.value = value
            self.remove(n)
            self.addToFront(n)


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
