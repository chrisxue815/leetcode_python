import unittest
from linkedlist import ListNode


class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type curr: ListNode
        :rtype: ListNode
        """
        curr = head
        while curr:
            next_ = curr.__next__
            while next_ and next_.val == curr.val:
                next_ = next_.__next__
            curr.next = next_
            curr = next_
        return head


class Test(unittest.TestCase):
    def test(self):
        self._test([1, 1, 2], [1, 2])
        self._test([1, 1, 2, 3, 3], [1, 2, 3])

    def _test(self, nums, expected):
        head = ListNode.from_array(nums)
        actual = Solution().deleteDuplicates(head)
        actual = ListNode.to_array(actual)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
