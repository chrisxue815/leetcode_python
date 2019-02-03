import unittest
from linkedlist import ListNode


def count(head):
    result = 0
    while head:
        result += 1
        head = head.__next__
    return result


class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        n = count(head)
        parent = ListNode(0)
        parent.next = head

        sublen = 1
        while True:
            new_sublen = sublen << 1
            prev = parent
            hi_node = prev.__next__

            for lo in range(0, n, new_sublen):
                lo_end = min(lo + sublen, n)
                hi = lo_end
                hi_end = min(hi + sublen, n)

                lo_node = hi_node
                for _ in range(hi - lo):
                    hi_node = hi_node.__next__

                for _ in range(hi_end - lo):
                    if hi >= hi_end or lo < lo_end and lo_node.val <= hi_node.val:
                        prev.next = lo_node
                        prev = lo_node
                        lo_node = lo_node.__next__
                        lo += 1
                    else:
                        prev.next = hi_node
                        prev = hi_node
                        hi_node = hi_node.__next__
                        hi += 1

            if new_sublen >= n:
                break
            sublen = new_sublen

        prev.next = None
        return parent.__next__


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
