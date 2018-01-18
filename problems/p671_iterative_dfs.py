import unittest
from tree import TreeNode


# O(n). Iterative DFS.
class Solution(object):
    def findSecondMinimumValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        result = 0x7FFFFFFF
        stack = []
        root_val = root.val
        node = root

        while node or stack:
            if node:
                if node.val != root_val:
                    result = min(result, node.val)
                    node = stack.pop() if stack else None
                elif node.left:
                    stack.append(node.right)
                    node = node.left
                else:
                    node = None
            else:
                node = stack.pop()

        return result if result != 0x7FFFFFFF else -1


class Test(unittest.TestCase):
    def test(self):
        self._test([2, 2, 5, None, None, 5, 7], 5)
        self._test([2, 2, 2], -1)

    def _test(self, root, expected):
        root = TreeNode.from_array(root)
        actual = Solution().findSecondMinimumValue(root)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
