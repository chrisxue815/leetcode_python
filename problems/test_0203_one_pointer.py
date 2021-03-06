import unittest
from linkedlist import ListNode


class Solution:
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        while head and head.val == val:
            head = head.next

        result = head
        while head and head.next:
            if head.next.val == val:
                head.next = head.next.next
            else:
                head = head.next
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
