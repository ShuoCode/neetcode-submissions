class Node:
    def __init__(self, key: int, val: int):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def insertNodeToFront(self, node: Node):
        first = self.head.next
        self.head.next = node
        node.next = first
        first.prev = node
        node.prev = self.head

    def removeNode(self, node: Node):
        prev = node.prev
        next = node.next
        prev.next = next
        next.prev = prev

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1

        node = self.cache[key]
        self.removeNode(node)
        self.insertNodeToFront(node)

        return self.cache[key].val 

    def put(self, key: int, value: int) -> None:
        if key not in self.cache:
            node = Node(key, value)
            self.insertNodeToFront(node)
            self.cache[key] = node
            if len(self.cache) > self.cap:
                lru = self.tail.prev
                self.removeNode(lru)
                del self.cache[lru.key]
            return
        
        self.cache[key].val = value
        self.removeNode(self.cache[key])
        self.insertNodeToFront(self.cache[key])