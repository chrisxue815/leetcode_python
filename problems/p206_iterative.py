import unittest
import utils
from linkedlist import ListNode


# O(n) time. O(1) space. Iteration.
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        prev = None
        while head:
            next_ = head.next
            head.next = prev
            prev = head
            head = next_
        return prev


class Test(unittest.TestCase):
    def test(self):
        cases = utils.load_json_from_path('../leetcode_test_cases/p206.json').test_cases

        for case in cases:
            head = ListNode.from_array(case.head)
            actual = Solution().reverseList(head)
            actual = ListNode.to_array(actual)
            self.assertEqual(case.expected, actual)


if __name__ == '__main__':
    unittest.main()
