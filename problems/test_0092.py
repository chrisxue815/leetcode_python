import unittest
from linkedlist import ListNode


class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        result = ListNode(0)
        result.next = head
        head = result
        for _ in range(m - 1):
            head = head.__next__

        left = head
        prev = None
        head = head.__next__
        right = head
        for _ in range(n - m + 1):
            next_ = head.__next__
            head.next = prev
            prev = head
            head = next_
        left.next = prev
        right.next = head

        return result.__next__


class Test(unittest.TestCase):
    def test(self):
        self._test([1, 2, 3, 4, 5], 2, 4, [1, 4, 3, 2, 5])
        self._test([1, 2, 3, 4, 5], 1, 5, [5, 4, 3, 2, 1])
        self._test([1, 2, 3, 4, 5], 1, 3, [3, 2, 1, 4, 5])
        self._test([1, 2, 3, 4, 5], 3, 5, [1, 2, 5, 4, 3])
        self._test([1, 2, 3, 4, 5], 5, 5, [1, 2, 3, 4, 5])
        self._test([1, 2, 3, 4, 5], 1, 1, [1, 2, 3, 4, 5])
        self._test([1], 1, 1, [1])

    def _test(self, head, m, n, expected):
        head = ListNode.from_array(head)

        actual = Solution().reverseBetween(head, m, n)

        actual = ListNode.to_array(actual)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
