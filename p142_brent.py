import unittest
from linkedlist import ListNode


class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return None

        t = head
        h = head.next
        max_loop_length = 1
        loop_length = 1

        while t is not h:
            if not h:
                return None

            if loop_length == max_loop_length:
                t = h
                max_loop_length <<= 1
                loop_length = 0

            h = h.next
            loop_length += 1

        h = head
        for i in xrange(loop_length):
            h = h.next

        t = head
        while t is not h:
            t = t.next
            h = h.next

        return t


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