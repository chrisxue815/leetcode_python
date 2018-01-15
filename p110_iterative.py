import unittest
from tree import TreeNode


class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        stack = []

        while root or stack:
            if root:
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
                    lh = root.left.height if root.left else 0
                    rh = root.right.height if root.right else 0
                    if abs(lh - rh) > 1:
                        return False
                    root.height = max(lh, rh) + 1
                    root = None
        return True


class Test(unittest.TestCase):
    def test_serialize(self):
        self._test([1, 2, 3], True)
        self._test([1, 2, 3, 4], True)
        self._test([1, 2, 3, 4, None, None, None, 5], False)
        self._test([1, 2, 3, 4, None, None, 5, 6, None, None, 7], False)

    def _test(self, root, expected):
        root = TreeNode.from_array(root)
        actual = Solution().isBalanced(root)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
