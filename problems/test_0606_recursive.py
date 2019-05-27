import unittest
from tree import TreeNode


class Solution:
    def tree2str(self, t):
        """
        :type t: TreeNode
        :rtype: str
        """
        if not t:
            return ''

        def dfs(node):
            result.append(str(node.val))
            if node.left:
                result.append('(')
                dfs(node.left)
                result.append(')')
            elif node.right:
                result.append('()')
            if node.right:
                result.append('(')
                dfs(node.right)
                result.append(')')

        result = []
        dfs(t)
        return ''.join(result)


class Test(unittest.TestCase):
    def test(self):
        self._test([1, 2, 3, 4], '1(2(4))(3)')
        self._test([1, 2, 3, None, 4], '1(2()(4))(3)')

    def _test(self, t, expected):
        t = TreeNode.from_array(t)
        actual = Solution().tree2str(t)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
