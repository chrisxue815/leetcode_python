import heapq
import unittest

from linkedlist import ListNode


class Solution:
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        if not lists:
            return None

        lists = [(head.val, head) for head in lists if head]

        heapq.heapify(lists)

        dummy = ListNode(0)
        curr = dummy

        while lists:
            val, prev = lists[0]
            curr.next = ListNode(val)
            curr = curr.next

            if prev.next:
                heapq.heapreplace(lists, (prev.next.val, prev.next))
            else:
                heapq.heappop(lists)

        return dummy.next


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
