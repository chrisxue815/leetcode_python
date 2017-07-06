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

        while curr.next and curr.next.next:
            a, b, c = curr.next, curr.next.next, curr.next.next.next
            curr.next = b
            b.next = a
            a.next = c
            curr = a

        return dummy.next


class Test(unittest.TestCase):
    def test(self):
        self._test([1, 2, 3, 4], [2, 1, 4, 3])
        self._test([1, 2, 3, 4, 5], [2, 1, 4, 3, 5])

    def _test(self, head, expected):
        head = ListNode.from_array(head)
        actual = Solution().swapPairs(head)
        actual = ListNode.to_array(actual)
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()
