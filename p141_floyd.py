import unittest
from linkedlist import ListNode


class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head:
            return False
        tortoise = head
        hare = head.next
        while tortoise is not hare:
            if not hare or not hare.next:
                return False
            hare = hare.next.next

            tortoise = tortoise.next
        return True


class Test(unittest.TestCase):
    def test(self):
        self._test([0, 1, 2, 3, 4, 5], 0, True)
        self._test([0, 1, 2, 3, 4, 5], 4, True)
        self._test([0, 1, 2, 3, 4, 5], 5, True)
        self._test([0, 1, 2, 3, 4, 5], -1, False)
        self._test([], -1, False)

    def _test(self, nums, loop_start_index, expected):
        root = ListNode.from_array(nums)

        if loop_start_index >= 0:
            loop_start_node = root
            for i in xrange(loop_start_index):
                loop_start_node = loop_start_node.next

            curr = loop_start_node
            while curr.next:
                curr = curr.next
            curr.next = loop_start_node

        actual = Solution().hasCycle(root)
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()
