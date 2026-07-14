class ListNode:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None


class MyHashMap:

    def __init__(self):
        self.size = 10 ** 4
        self.map = [ListNode(0, 0) for i in range(self.size)]

    def put(self, key: int, value: int) -> None:
        hashed = key % self.size
        head = self.map[hashed]

        while head.next:
            if head.next.key == key:
                head.next.val = value
                return
            head = head.next
        head.next = ListNode(key, value)

    def get(self, key: int) -> int:
        hashed = key % self.size
        head = self.map[hashed]

        while head.next:
            if head.next.key == key:
                return head.next.val
            head = head.next
        return -1

    def remove(self, key: int) -> None:
        hashed = key % self.size
        head = self.map[hashed]

        while head.next:
            if head.next.key == key:
                head.next = head.next.next
                return
            head = head.next
