import unittest
from linkedlist import ListNode


def _sort(lo):
    if not lo.next:
        return lo

    mid = lo
    tail = lo
    while tail and tail.next and tail.next.next:
        mid = mid.next
        tail = tail.next.next

    hi = mid.next
    mid.next = None

    lo = _sort(lo)
    hi = _sort(hi)

    dummy = ListNode(0)
    prev = dummy
    while lo and hi:
        if lo.val <= hi.val:
            prev.next = lo
            prev = lo
            lo = lo.next
        else:
            prev.next = hi
            prev = hi
            hi = hi.next

    if lo:
        prev.next = lo
    else:
        prev.next = hi

    return dummy.next


class Solution:
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return None

        return _sort(head)


class Test(unittest.TestCase):
    def test(self):
        self._test([5, 3, 6, 1, 8, 7, 2, 4], [1, 2, 3, 4, 5, 6, 7, 8])
        self._test([5, 3, 6, 1, 7, 2, 4], [1, 2, 3, 4, 5, 6, 7])
        self._test([5, 3, 6, 1, 2, 4], [1, 2, 3, 4, 5, 6])
        self._test([5, 3, 1, 2, 4], [1, 2, 3, 4, 5])
        self._test([1], [1])
        self._test([], [])

    def _test(self, head, expected):
        head = ListNode.from_array(head)

        actual = Solution().sortList(head)

        actual = ListNode.to_array(actual)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
