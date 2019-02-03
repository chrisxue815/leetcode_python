import unittest
from linkedlist import ListNode


class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(0)
        dummy.next = head
        curr = dummy

        while curr.__next__ and curr.next.__next__:
            a, b, c = curr.__next__, curr.next.__next__, curr.next.next.__next__
            curr.next = b
            b.next = a
            a.next = c
            curr = a

        return dummy.__next__


class Test(unittest.TestCase):
    def test(self):
        self._test([1, 2, 3, 4], [2, 1, 4, 3])
        self._test([1, 2, 3, 4, 5], [2, 1, 4, 3, 5])

    def _test(self, head, expected):
        head = ListNode.from_array(head)
        actual = Solution().swapPairs(head)
        actual = ListNode.to_array(actual)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
