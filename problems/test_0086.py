import unittest
from linkedlist import ListNode


class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        small_head = ListNode(0)
        small_curr = small_head
        large_head = ListNode(0)
        large_curr = large_head

        while head:
            if head.val < x:
                small_curr.next = head
                small_curr = head
            else:
                large_curr.next = head
                large_curr = head
            head = head.next

        small_curr.next = large_head.next
        large_curr.next = None
        return small_head.next


class Test(unittest.TestCase):
    def test(self):
        self._test([1, 4, 3, 2, 5, 2], 3, [1, 2, 2, 4, 3, 5])
        self._test([1, 4, 2, 5, 2, 3], 3, [1, 2, 2, 4, 5, 3])
        self._test([3, 1, 4, 2, 5, 2], 3, [1, 2, 2, 3, 4, 5])
        self._test([1], 3, [1])
        self._test([], 3, [])

    def _test(self, head, x, expected):
        head = ListNode.from_array(head)

        actual = Solution().partition(head, x)

        actual = ListNode.to_array(actual)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
