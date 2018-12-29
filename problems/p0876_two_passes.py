import unittest
import utils
from linkedlist import ListNode


# O(n) time. O(1) space. Iteration.
class Solution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        length = 0
        curr = head
        while curr:
            length += 1
            curr = curr.next

        for _ in xrange(length // 2):
            head = head.next

        return head


class Test(unittest.TestCase):
    def test(self):
        cases = utils.load_test_json(__file__).test_cases

        for case in cases:
            head = ListNode.from_array(case.head)
            actual = Solution().middleNode(head)
            actual = actual.val
            self.assertEqual(case.expected, actual)


if __name__ == '__main__':
    unittest.main()
