# Definition for singly-linked list with a random pointer.
class RandomListNode(object):
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None


class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        if not head:
            return None

        curr = head

        while curr:
            curr.clone = RandomListNode(curr.label)
            curr = curr.next

        curr = head
        while curr:
            curr.clone.next = curr.next.clone if curr.next else None
            curr.clone.random = curr.random.clone if curr.random else None
            curr = curr.next

        return head.clone
