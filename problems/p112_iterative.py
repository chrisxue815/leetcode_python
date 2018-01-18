import unittest
from tree import TreeNode


class Solution(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if not root:
            return False

        stack = []

        while root or stack:
            if root:
                sum -= root.val
                if root.right:
                    stack.append(root.right)
                stack.append(root)
                root = root.left
            else:
                root = stack.pop()
                if stack and stack[-1] is root.right:
                    stack[-1] = root
                    root = root.right
                else:
                    if not root.left and not root.right and not sum:
                        return True
                    sum += root.val
                    root = None
        return False


class Test(unittest.TestCase):
    def test_serialize(self):
        self._test([5, 4, 8, 11, None, 13, 4, 7, 2, None, None, None, 1], 22, True)
        self._test([], 0, False)

    def _test(self, root, sum, expected):
        root = TreeNode.from_array(root)
        actual = Solution().hasPathSum(root, sum)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
