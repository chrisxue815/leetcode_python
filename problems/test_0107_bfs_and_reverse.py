import unittest
from tree import TreeNode


class Solution:
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []

        result = []
        q = [root]

        while q:
            level = []
            next_q = []

            for node in q:
                level.append(node.val)
                if node.left:
                    next_q.append(node.left)
                if node.right:
                    next_q.append(node.right)

            result.append(level)
            q = next_q

        result.reverse()
        return result


class Test(unittest.TestCase):
    def test(self):
        self._test(
            [3, 9, 20, None, None, 15, 7],
            [
                [15, 7],
                [9, 20],
                [3],
            ])

    def _test(self, root, expected):
        root = TreeNode.from_array(root)
        actual = Solution().levelOrderBottom(root)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
