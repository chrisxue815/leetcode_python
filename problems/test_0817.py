import unittest
import utils
from linkedlist import ListNode


# O(n) time. O(n) space. Linked-list.
class Solution(object):
    def numComponents(self, head, g):
        """
        :type head: ListNode
        :type g: List[int]
        :rtype: int
        """
        result = 0
        g = set(g)
        prev_in_g = False

        while head:
            curr_in_g = head.val in g
            if curr_in_g and not prev_in_g:
                result += 1
            prev_in_g = curr_in_g
            head = head.next

        return result


class Test(unittest.TestCase):
    def test(self):
        cases = utils.load_test_json(__file__).test_cases

        for case in cases:
            head = ListNode.from_array(case.args.head)
            actual = Solution().numComponents(head, case.args.g)
            self.assertEqual(case.expected, actual, msg=case.args)


if __name__ == '__main__':
    unittest.main()
