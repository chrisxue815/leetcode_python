import unittest
from linkedlist import ListNode


class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        if not node or not node.next:
            return node

        while True:
            node.val = node.next.val
            if not node.next.next:
                node.next = None
                break
            node = node.next


class Test(unittest.TestCase):
    def test(self):
        self._test([1, 2, 3, 4], [2, 3, 4])
        self._test([1], [1])
        self._test([], [])

    def _test(self, node, expected):
        node = ListNode.from_array(node)

        Solution().deleteNode(node)

        actual = ListNode.to_array(node)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
