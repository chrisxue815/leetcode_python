import unittest
from linkedlist import ListNode


def count(head):
    result = 0
    while head:
        result += 1
        head = head.next
    return result


class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head:
            return True

        length = count(head)
        prev = None

        for _ in xrange(length >> 1):
            next_ = head.next
            head.next = prev
            prev = head
            head = next_

        if length & 1:
            head = head.next

        while prev and prev.val == head.val:
            prev = prev.next
            head = head.next
        return not prev


class Test(unittest.TestCase):
    def test(self):
        self._test([1, 2, 1], True)
        self._test([1, 2, 2, 1], True)
        self._test([1, 2, 3], False)
        self._test([1], True)
        self._test([], True)

    def _test(self, head, expected):
        head = ListNode.from_array(head)

        actual = Solution().isPalindrome(head)
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()
