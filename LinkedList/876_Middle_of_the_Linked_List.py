from typing import Optional

from LinkedList.ListNode import ListNode


class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        count = 0

        curr = head
        while curr:
            curr = curr.next
            count += 1

        middle = count // 2

        curr = head
        for i in range(middle):
            curr = curr.next

        return curr
