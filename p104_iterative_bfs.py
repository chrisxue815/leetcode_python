import unittest
from tree import TreeNode


class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0

        q = [root]
        depth = 0

        while q:
            depth += 1
            new_q = []
            for root in q:
                if root.left:
                    new_q.append(root.left)
                if root.right:
                    new_q.append(root.right)
            q = new_q
            
        return depth


class Test(unittest.TestCase):
    def test_serialize(self):
        self._test([1, 1, 1, None, 1, 1, None, None, None, 1, None], 4)

    def _test(self, vals, expected):
        root = TreeNode.from_array(vals)
        actual = Solution().maxDepth(root)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
