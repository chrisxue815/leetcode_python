import unittest
from linkedlist import ListNode


class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: void Do not return anything, modify head in-place instead.
        """
        if not head:
            return

        mid = head
        tail = head
        while tail and tail.__next__ and tail.next.__next__:
            mid = mid.__next__
            tail = tail.next.__next__

        curr = mid.__next__
        mid.next = None
        tail = None
        while curr:
            next_ = curr.__next__
            curr.next = tail
            tail = curr
            curr = next_

        while tail:
            head_next = head.__next__
            head.next = tail
            head = head_next

            tail_next = tail.__next__
            tail.next = head_next
            tail = tail_next


class Test(unittest.TestCase):
    def test(self):
        self._test([1, 2, 3, 4], [1, 4, 2, 3])
        self._test([1, 2, 3, 4, 5], [1, 5, 2, 4, 3])
        self._test([1, 2], [1, 2])
        self._test([1], [1])
        self._test([], [])

    def _test(self, head, expected):
        head = ListNode.from_array(head)

        Solution().reorderList(head)

        actual = ListNode.to_array(head)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
