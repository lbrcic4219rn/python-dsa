from LinkedList.ListNode import ListNode


class Solution:
    def removeNodes(self, head: ListNode | None) -> ListNode | None:
        def reverse(node):
            prev = None
            curr = node
            while curr:
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt
            return prev

        curr = head = reverse(head)
        currMax = head.val
        while curr:
            currMax = max(currMax, curr.val)
            nxt = curr.next
            while nxt and currMax > nxt.val:
                nxt = nxt.next
            curr.next = nxt
            curr = nxt
        return reverse(head)
