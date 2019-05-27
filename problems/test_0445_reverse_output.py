import unittest
from linkedlist import ListNode


def count(root):
    result = 0
    while root:
        result += 1
        root = root.next
    return result


class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if not l2:
            return l1
        if not l1:
            return l2

        len1 = count(l1)
        len2 = count(l2)

        if len1 < len2:
            l1, l2 = l2, l1
            len1, len2 = len2, len1

        result_root = ListNode(0)
        result = result_root

        for i in range(len1 - len2):
            right = ListNode(l1.val)
            right.next = result
            result = right
            l1 = l1.next

        while l1:
            right = ListNode(l1.val + l2.val)
            right.next = result
            result = right

            l1 = l1.next
            l2 = l2.next

        right = None
        carry = 0
        while result:
            result.val += carry
            if result.val >= 10:
                result.val -= 10
                carry = 1
            else:
                carry = 0

            left = result.next
            result.next = right
            right = result
            result = left

        return result_root if result_root.val else result_root.next


class Test(unittest.TestCase):
    def test(self):
        self._test([3, 4, 2], [4, 6, 5], [8, 0, 7])
        self._test([7, 2, 4, 3], [5, 6, 4], [7, 8, 0, 7])

    def _test(self, l1, l2, expected):
        l1 = ListNode.from_array(l1)
        l2 = ListNode.from_array(l2)

        actual = Solution().addTwoNumbers(l1, l2)
        actual = ListNode.to_array(actual)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
