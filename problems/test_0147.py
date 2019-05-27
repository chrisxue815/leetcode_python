import unittest
from linkedlist import ListNode


class Solution:
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
            while curr.next and curr.next.val < val:
                curr = curr.next
            next_ = head.next
            head.next = curr.next
            curr.next = head
            head = next_

        return sorted_head.next


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
