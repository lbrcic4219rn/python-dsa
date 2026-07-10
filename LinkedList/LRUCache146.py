class Node:
    def __init__(self, val, key):
        self.val = val
        self.key = key
        self.next = None
        self.prev = None


class LRUCache:

    def __init__(self, capacity: int):
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.cap = capacity
        self.map = {}

    def remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def inset(self, node):
        node.next = self.tail
        node.prev = self.tail.prev
        self.tail.prev.next = node
        self.tail.prev = node

    def get(self, key: int) -> int:
        if key in self.map:
            self.remove(self.map[key])
            self.inset(self.map[key])
            return self.map[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.map:
            self.remove(self.map[key])

        node = Node(value, key)
        self.map[key] = node
        self.inset(node)
        if len(self.map) > self.cap:
            lru = self.head.next
            self.remove(lru)
            del self.map[lru.key]
