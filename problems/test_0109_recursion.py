import unittest
from linkedlist import ListNode
from tree import TreeNode


def count(head):
    result = 0
    while head:
        result += 1
        head = head.next
    return result


def _to_bst(head, length):
    if not length:
        return None, head
    if length == 1:
        return TreeNode(head.val), head.next

    left_length = length >> 1
    left, head = _to_bst(head, left_length)
    root = TreeNode(head.val)
    right, head = _to_bst(head.next, length - left_length - 1)

    root.left = left
    root.right = right
    return root, head


class Solution:
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        length = count(head)
        return _to_bst(head, length)[0]


class Test(unittest.TestCase):
    def test(self):
        self._test([1, 2, 3, 4, 5, 6, 7], [4, 2, 6, 1, 3, 5, 7])
        self._test([1, 2, 3, 4, 5], [3, 2, 5, 1, None, 4])
        self._test([], [])

    def _test(self, linked_list, expected):
        linked_list = ListNode.from_array(linked_list)

        actual = Solution().sortedListToBST(linked_list)
        actual = TreeNode.to_array_static(actual)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
