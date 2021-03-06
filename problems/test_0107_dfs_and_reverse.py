import unittest
from tree import TreeNode


def _dfs(root, depth, result):
    if not root:
        return
    if len(result) == depth:
        result.append([root.val])
    else:
        result[depth].append(root.val)
    _dfs(root.left, depth + 1, result)
    _dfs(root.right, depth + 1, result)


class Solution:
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        result = []
        _dfs(root, 0, result)

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
