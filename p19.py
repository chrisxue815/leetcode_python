import unittest
from linkedlist import ListNode


class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        dummy = ListNode(0)
        dummy.next = head
        lo = dummy

        for _ in xrange(n):
            head = head.next

        while head:
            head = head.next
            lo = lo.next

        lo.next = lo.next.next

        return dummy.next


class Test(unittest.TestCase):
    def test(self):
        self._test([1, 2, 3, 4, 5], 2, [1, 2, 3, 5])
        self._test([1, 2, 3, 4, 5], 5, [2, 3, 4, 5])

    def _test(self, head, n, expected):
        head = ListNode.from_array(head)

        actual = Solution().removeNthFromEnd(head, n)

        actual = ListNode.to_array(actual)
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()
