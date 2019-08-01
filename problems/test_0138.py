# Definition for a Node.
class Node:
    def __init__(self, val, next, random):
        self.val = val
        self.next = next
        self.random = random


# O(n) time. O(1) space.
class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head:
            return None

        curr = head
        while curr:
            clone = Node(curr.val, curr.next, None)
            curr.next = clone
            curr = clone.next

        clone_head = head.next

        curr = head
        while curr:
            clone = curr.next
            nxt = clone.next
            if curr.random:
                clone.random = curr.random.next
            curr = nxt

        curr = head
        while curr:
            clone = curr.next
            nxt = clone.next
            if nxt:
                clone.next = nxt.next
            curr.next = nxt
            curr = nxt

        return clone_head
