import unittest
from linkedlist import ListNode
import heapq


class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        if not lists:
            return None

        ListNode.__cmp__ = lambda x, y: x.val - y.val

        lists = [head for head in lists if head]

        heapq.heapify(lists)

        dummy = ListNode(0)
        curr = dummy

        while lists:
            curr.next = ListNode(lists[0].val)
            curr = curr.__next__

            if lists[0].__next__:
                heapq.heapreplace(lists, lists[0].__next__)
            else:
                heapq.heappop(lists)

        return dummy.__next__


class Test(unittest.TestCase):
    def test(self):
        self._test([[2, 6], [1, 4], [3, 5], [7], []], [1, 2, 3, 4, 5, 6, 7])
        self._test([], [])

    def _test(self, lists, expected):
        lists = [ListNode.from_array(l) for l in lists]

        actual = Solution().mergeKLists(lists)

        actual = ListNode.to_array(actual)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
