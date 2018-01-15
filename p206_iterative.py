import unittest
from linkedlist import ListNode


class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        prev = None
        while head:
            next_ = head.next
            head.next = prev
            prev = head
            head = next_
        return prev


class Test(unittest.TestCase):
    def test(self):
        self._test([1, 2, 3], [3, 2, 1])
        self._test([1], [1])
        self._test([], [])

    def _test(self, head, expected):
        head = ListNode.from_array(head)

        actual = Solution().reverseList(head)
        actual = ListNode.to_array(actual)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
