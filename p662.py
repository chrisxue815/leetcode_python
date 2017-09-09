import unittest
from tree import TreeNode


class Solution(object):
    def widthOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0

        result = 1
        q = [(root, 0)]

        while q:
            result = max(result, q[-1][1] - q[0][1] + 1)
            next_q = []
            for node, i in q:
                if node.left:
                    next_q.append((node.left, i << 1))
                if node.right:
                    next_q.append((node.right, (i << 1) + 1))
            q = next_q

        return result


class Test(unittest.TestCase):
    def test_serialize(self):
        self._test([1, 3, 2, 5, None, None, 9, 6, None, None, 7], 8)

    def _test(self, root, expected):
        root = TreeNode.from_array(root)
        actual = Solution().widthOfBinaryTree(root)
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()
