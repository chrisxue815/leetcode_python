import unittest
from linkedlist import ListNode


class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(0)
        prev = dummy

        while l1 and l2:
            if l1.val < l2.val:
                prev.next = l1
                prev = l1
                l1 = l1.next
            else:
                prev.next = l2
                prev = l2
                l2 = l2.next
        prev.next = l1 if l1 else l2
        return dummy.next


class Test(unittest.TestCase):
    def test(self):
        self._test([1, 3, 4], [2, 5, 6], [1, 2, 3, 4, 5, 6])

    def _test(self, l1, l2, expected):
        l1 = ListNode.from_array(l1)
        l2 = ListNode.from_array(l2)
        actual = Solution().mergeTwoLists(l1, l2)
        actual = ListNode.to_array(actual)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
