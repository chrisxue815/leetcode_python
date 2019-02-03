import unittest
from linkedlist import ListNode


def _sort(lo):
    if not lo.__next__:
        return lo

    mid = lo
    tail = lo
    while tail and tail.__next__ and tail.next.__next__:
        mid = mid.__next__
        tail = tail.next.__next__

    hi = mid.__next__
    mid.next = None

    lo = _sort(lo)
    hi = _sort(hi)

    dummy = ListNode(0)
    prev = dummy
    while lo and hi:
        if lo.val <= hi.val:
            prev.next = lo
            prev = lo
            lo = lo.__next__
        else:
            prev.next = hi
            prev = hi
            hi = hi.__next__

    if lo:
        prev.next = lo
    else:
        prev.next = hi

    return dummy.__next__


class Solution(object):
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
