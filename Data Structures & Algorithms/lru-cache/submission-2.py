class Node:
    def __init__(self, key: int, value: int):
        self.key = key
        self.value = value
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

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1

        if key != self.head.next.key:
            self._moveNodeToHead(key)
        
        return self.cache[key].value

    def put(self, key: int, value: int) -> None:
        if key not in self.cache:
            self.cache[key] = Node(key, value) # create new node
            self._insertNodeToHead(key, value)
            
            if len(self.cache) > self.cap:
                del self.cache[self._removeNodeFromTail()]

            return None

        if self.cache[key].value != value:
            self.cache[key].value = value
            self._insertNodeToHead(key, value)
            return None
    
    def _insertNodeToHead(self, key: int, value: int):
        self.cache[key].prev = self.head
        self.cache[key].next = self.head.next
        self.head.next.prev = self.cache[key]
        self.head.next = self.cache[key]

    def _removeNodeFromTail(self) -> int:
        key = self.tail.prev.key
        self.tail.prev.prev.next = self.tail
        self.tail.prev = self.tail.prev.prev
        return key

    def _moveNodeToHead(self, key: int):
        self.cache[key].prev.next = self.cache[key].next
        self.cache[key].next.prev = self.cache[key].prev
        self._insertNodeToHead(key, self.cache[key].value)