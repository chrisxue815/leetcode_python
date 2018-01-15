import unittest
from tree import TreeNode


class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        q = [root]
        depth = 1

        while q:
            new_q = []
            for node in q:
                if not node.left and not node.right:
                    return depth
                if node.left:
                    new_q.append(node.left)
                if node.right:
                    new_q.append(node.right)
            q = new_q
            depth += 1


class Test(unittest.TestCase):
    def test_serialize(self):
        self._test([5, 4, 8, 11, None, 13, 4, 7, 2, None, None, None, 1], 3)
        self._test([], 0)
        self._test([1], 1)

    def _test(self, root, expected):
        root = TreeNode.from_array(root)
        actual = Solution().minDepth(root)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
