import unittest
from tree import TreeNode


# O(n). BFS.
class Solution(object):
    def findSecondMinimumValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return -1

        result = 0x7FFFFFFF
        root_val = root.val
        q = [root]

        while q:
            next_q = []
            for node in q:
                if node.val != root_val:
                    result = min(result, node.val)
                elif node.left:
                    next_q.append(node.left)
                    next_q.append(node.right)
            q = next_q

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
