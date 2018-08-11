import unittest
import utils
from linkedlist import ListNode


# O(n) time. O(1) space. Iteration.
class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        odd_head = ListNode(0)
        odd = odd_head
        even_head = ListNode(0)
        even = even_head

        while True:
            if not head:
                break
            odd.next = head
            odd = head
            head = head.next

            if not head:
                break
            even.next = head
            even = head
            head = head.next

        odd.next = even_head.next
        even.next = None
        return odd_head.next


class Test(unittest.TestCase):
    def test(self):
        cases = utils.load_json_from_path('../leetcode_test_cases/p328.json').test_cases

        for case in cases:
            head = ListNode.from_array(case.head)
            actual = Solution().oddEvenList(head)
            actual = ListNode.to_array(actual)
            self.assertEqual(case.expected, actual)


if __name__ == '__main__':
    unittest.main()
