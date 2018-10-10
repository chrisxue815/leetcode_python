import unittest
import utils
from linkedlist import ListNode


class Solution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        slow = head
        fast = head

        while fast:
            fast = fast.next
            if fast:
                fast = fast.next
            else:
                break

            slow = slow.next

        return slow


class Test(unittest.TestCase):
    def test(self):
        cases = utils.load_json_from_path('../leetcode_test_cases/p876.json').test_cases

        for case in cases:
            head = ListNode.from_array(case.head)
            actual = Solution().middleNode(head)
            actual = actual.val
            self.assertEqual(case.expected, actual)


if __name__ == '__main__':
    unittest.main()
