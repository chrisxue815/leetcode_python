import unittest
from tree import TreeNode


class Solution:
    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        if not root:
            return False

        q = [root]
        visited = set()
        for node in q:
            if k - node.val in visited:
                return True
            visited.add(node.val)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)

        return False


class Test(unittest.TestCase):
    def test(self):
        self._test([5, 3, 6, 2, 4, None, 7], 9, True)
        self._test([5, 3, 6, 2, 4, None, 7], 28, False)
        self._test([1], 2, False)

    def _test(self, root, k, expected):
        root = TreeNode.from_array(root)
        actual = Solution().findTarget(root, k)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
