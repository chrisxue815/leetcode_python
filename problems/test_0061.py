import unittest
from linkedlist import ListNode


class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head or not k:
            return head

        length = 1
        tail = head
        while tail.next:
            length += 1
            tail = tail.next

        k %= length
        if not k:
            return head

        tail.next = head

        for _ in range(length - k - 1):
            head = head.next

        new_head = head.next
        head.next = None
        return new_head


class Test(unittest.TestCase):
    def test(self):
        self._test([1, 2, 3, 4, 5], 2, [4, 5, 1, 2, 3])
        self._test([1, 2, 3, 4, 5], 7, [4, 5, 1, 2, 3])
        self._test([1, 2, 3, 4, 5], 0, [1, 2, 3, 4, 5])
        self._test([1, 2, 3, 4, 5], 5, [1, 2, 3, 4, 5])
        self._test([], 2, [])

    def _test(self, head, k, expected):
        head = ListNode.from_array(head)

        actual = Solution().rotateRight(head, k)

        actual = ListNode.to_array(actual)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
