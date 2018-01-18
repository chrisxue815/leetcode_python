import unittest
from linkedlist import ListNode


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
            right = ListNode(head.val)
            odd.next = right
            odd = right
            head = head.next

            if not head:
                break
            right = ListNode(head.val)
            even.next = right
            even = right
            head = head.next

        odd.next = even_head.next
        return odd_head.next


class Test(unittest.TestCase):
    def test(self):
        self._test([1, 2, 3, 4, 5], [1, 3, 5, 2, 4])
        self._test([2, 3, 4, 5, 6], [2, 4, 6, 3, 5])
        self._test([1], [1])
        self._test([], [])

    def _test(self, head, expected):
        head = ListNode.from_array(head)

        actual = Solution().oddEvenList(head)
        actual = ListNode.to_array(actual)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
