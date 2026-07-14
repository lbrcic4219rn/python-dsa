class ListNode:
    def __init__(self, val: int):
        self.val = val
        self.next = None


class MyHashSet:

    def __init__(self):
        self.size = 10 ** 4
        self.set = [ListNode(0) for _ in range(self.size)]

    def add(self, key: int) -> None:
        hashedKey = key % self.size
        head = self.set[hashedKey]
        while head.next:
            if head.next.val == key:
                return
            head = head.next
        head.next = ListNode(key)

    def remove(self, key: int) -> None:
        hashedKey = key % self.size
        head = self.set[hashedKey]
        while head.next:
            if head.next.val == key:
                head.next = head.next.next
                return
            head = head.next

    def contains(self, key: int) -> bool:
        hashedKey = key % self.size
        head = self.set[hashedKey]
        while head.next:
            if head.next.val == key:
                return True
            head = head.next
        return False
