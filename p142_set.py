import unittest
from linkedlist import ListNode


class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        visited = set()

        while head:
            if head in visited:
                return head
            visited.add(head)
            head = head.next
        return None


class Test(unittest.TestCase):
    def test(self):
        self._test([0, 1, 2, 3, 4, 5], 0)
        self._test([0, 1, 2, 3, 4, 5], 4)
        self._test([0, 1, 2, 3, 4, 5], 5)
        self._test([0, 1, 2, 3, 4, 5], -1)

    def _test(self, nums, loop_start_index):
        root = ListNode.from_array(nums)

        if loop_start_index < 0:
            loop_start_node = None
        else:
            loop_start_node = root
            for i in xrange(loop_start_index):
                loop_start_node = loop_start_node.next

            if not loop_start_node.next:
                loop_start_node.next = loop_start_node
            else:
                curr = loop_start_node
                while curr.next:
                    curr = curr.next
                curr.next = loop_start_node

        actual = Solution().detectCycle(root)
        self.assertEqual(actual, loop_start_node)


if __name__ == '__main__':
    unittest.main()
