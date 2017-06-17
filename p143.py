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
        while tail and tail.next and tail.next.next:
            mid = mid.next
            tail = tail.next.next

        curr = mid.next
        mid.next = None
        tail = None
        while curr:
            next_ = curr.next
            curr.next = tail
            tail = curr
            curr = next_

        while tail:
            head_next = head.next
            head.next = tail
            head = head_next

            tail_next = tail.next
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
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()
