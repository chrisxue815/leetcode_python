import unittest
from linkedlist import ListNode


def _reverse_list(head):
    if head and head.next:
        new_head, new_tail = _reverse_list(head.next)
        new_tail.next = head
        return new_head, head
    else:
        return head, head


class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return None
        head, tail = _reverse_list(head)
        tail.next = None
        return head


class Test(unittest.TestCase):
    def test(self):
        self._test([1, 2, 3], [3, 2, 1])
        self._test([1], [1])
        self._test([], [])

    def _test(self, head, expected):
        head = ListNode.from_array(head)

        actual = Solution().reverseList(head)
        actual = ListNode.to_array(actual)
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()
