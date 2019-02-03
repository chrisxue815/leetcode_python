import unittest
from linkedlist import ListNode


class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        while head and head.val == val:
            head = head.__next__

        if not head:
            return None

        result = head
        prev = head
        head = head.__next__
        while head:
            if head.val == val:
                prev.next = head.__next__
            else:
                prev = head
            head = head.__next__
        return result


class Test(unittest.TestCase):
    def test(self):
        self._test([1, 2, 6, 3, 4, 5, 6], 6, [1, 2, 3, 4, 5])
        self._test([1], 6, [1])
        self._test([1, 6, 6, 1], 6, [1, 1])
        self._test([6], 6, [])
        self._test([], 6, [])

    def _test(self, head, x, expected):
        head = ListNode.from_array(head)

        actual = Solution().removeElements(head, x)

        actual = ListNode.to_array(actual)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
