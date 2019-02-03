import unittest
from linkedlist import ListNode


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        carry = 0
        sum_root = ListNode(0)
        sum_ = sum_root
        while l1 and l2:
            digit = l1.val + l2.val + carry
            if digit >= 10:
                digit -= 10
                carry = 1
            else:
                carry = 0
            node = ListNode(digit)
            sum_.next = node
            sum_ = node

            l1 = l1.next
            l2 = l2.next

        if l2:
            l1 = l2

        while l1:
            digit = l1.val + carry
            if digit >= 10:
                digit -= 10
                carry = 1
            else:
                carry = 0
            node = ListNode(digit)
            sum_.next = node
            sum_ = node

            l1 = l1.next
        if carry:
            sum_.next = ListNode(carry)
        return sum_root.next


class Test(unittest.TestCase):
    def test(self):
        self._test([2, 4, 3], [5, 6, 4], [7, 0, 8])

    def _test(self, l1, l2, expected):
        l1 = ListNode.from_array(l1)
        l2 = ListNode.from_array(l2)

        actual = Solution().addTwoNumbers(l1, l2)
        actual = ListNode.to_array(actual)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
