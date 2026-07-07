from typing import Optional

from LinkedList.ListNode import Node


class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head is None:
            return None

        curr = head
        while curr:
            currCopy = Node(curr.val, curr.next, None)
            curr.next = currCopy
            curr = currCopy.next

        curr = head
        while curr:
            if curr.random:
                curr.next.random = curr.random.next
            curr = curr.next.next
        newHead = head.next

        l1 = head
        while l1:
            l2 = l1.next
            l1.next = l2.next
            if l2.next:
                l2.next = l2.next.next
            l1 = l1.next

        return newHead
