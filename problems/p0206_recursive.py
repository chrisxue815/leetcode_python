import unittest
import utils
from linkedlist import ListNode


def _reverse_list(curr, prev):
    next_ = curr.next
    curr.next = prev

    if not next_:
        return curr

    return _reverse_list(next_, curr)


# O(n) time. O(n) space. Tail recursion.
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return None

        head = _reverse_list(head, None)
        return head


class Test(unittest.TestCase):
    def test(self):
        cases = utils.load_test_json(__file__).test_cases

        for case in cases:
            head = ListNode.from_array(case.args.head)
            actual = Solution().reverseList(head)
            actual = ListNode.to_array(actual)
            self.assertEqual(case.expected, actual)


if __name__ == '__main__':
    unittest.main()
