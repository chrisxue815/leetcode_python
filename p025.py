import unittest
from linkedlist import ListNode


class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head or k == 1:
            return head

        length = 0
        curr = head
        while curr:
            length += 1
            curr = curr.next

        if k > length:
            return head

        tail = head
        prev = head
        curr = head.next
        for _ in xrange(k - 1):
            next_ = curr.next
            curr.next = prev
            prev = curr
            curr = next_
        if not curr:
            tail.next = None
            return prev
        head = prev
        length -= k

        while length >= k:
            next_tail = curr
            prev = curr
            curr = curr.next
            for _ in xrange(k - 1):
                next_ = curr.next
                curr.next = prev
                prev = curr
                curr = next_
            tail.next = prev
            tail = next_tail
            length -= k

        tail.next = curr

        return head


class Test(unittest.TestCase):
    def test(self):
        self._test([1, 2, 3, 4, 5], 2, [2, 1, 4, 3, 5])
        self._test([1, 2, 3, 4, 5], 3, [3, 2, 1, 4, 5])
        self._test([1, 2, 3, 4, 5], 5, [5, 4, 3, 2, 1])
        self._test([1, 2, 3, 4, 5], 1, [1, 2, 3, 4, 5])
        self._test([1, 2, 3, 4, 5, 6], 2, [2, 1, 4, 3, 6, 5])
        self._test([], 2, [])

    def _test(self, head, k, expected):
        head = ListNode.from_array(head)

        actual = Solution().reverseKGroup(head, k)

        actual = ListNode.to_array(actual)
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()
