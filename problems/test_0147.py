import unittest
from linkedlist import ListNode


class Solution(object):
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return None

        sorted_head = ListNode(0)

        while head:
            val = head.val
            curr = sorted_head
            while curr.__next__ and curr.next.val < val:
                curr = curr.__next__
            next_ = head.__next__
            head.next = curr.__next__
            curr.next = head
            head = next_

        return sorted_head.__next__


class Test(unittest.TestCase):
    def test(self):
        self._test([4, 2, 6, 1, 3, 5, 7], [1, 2, 3, 4, 5, 6, 7])
        self._test([1], [1])
        self._test([], [])

    def _test(self, head, expected):
        head = ListNode.from_array(head)

        actual = Solution().insertionSortList(head)

        actual = ListNode.to_array(actual)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
