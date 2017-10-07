import unittest
from tree import TreeNode


# O(n). Recursive DFS.
class Solution(object):
    def findSecondMinimumValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return -1
        root_val = root.val

        def find_min(node):
            if not node:
                return 0x7FFFFFFF
            if node.val != root_val:
                return node.val
            return min(find_min(node.left), find_min(node.right))

        sec_min = find_min(root)
        return sec_min if sec_min != 0x7FFFFFFF else -1


class Test(unittest.TestCase):
    def test(self):
        self._test([2, 2, 5, None, None, 5, 7], 5)
        self._test([2, 2, 2], -1)

    def _test(self, root, expected):
        root = TreeNode.from_array(root)
        actual = Solution().findSecondMinimumValue(root)
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()
