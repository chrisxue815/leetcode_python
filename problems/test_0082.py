import unittest
from linkedlist import ListNode


class Solution:
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return None

        parent = ListNode(head.val - 1)
        parent.next = head
        head = parent

        while head.next and head.next.next:
            val = head.next.val
            if head.next.next.val == val:
                next_ = head.next.next.next
                while next_ and next_.val == val:
                    next_ = next_.next
                head.next = next_
            else:
                head = head.next

        return parent.next


class Test(unittest.TestCase):
    def test(self):
        self._test([1, 2, 3, 3, 4, 4, 5], [1, 2, 5])
        self._test([1, 1, 1, 2, 3], [2, 3])

    def _test(self, head, expected):
        head = ListNode.from_array(head)

        actual = Solution().deleteDuplicates(head)

        actual = ListNode.to_array(actual)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
