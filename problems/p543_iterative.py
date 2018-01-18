import unittest
from tree import TreeNode


class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type curr: TreeNode
        :rtype: int
        """
        if not root:
            return 0

        stack = []
        curr = root
        while curr or stack:
            if curr:
                if curr.right:
                    stack.append(curr.right)
                stack.append(curr)
                curr = curr.left
            else:
                curr = stack.pop()
                if stack and curr.right is stack[-1]:
                    curr, stack[-1] = stack[-1], curr
                else:
                    lh, ld = (curr.left.height, curr.left.diameter) if curr.left else (0, 0)
                    rh, rd = (curr.right.height, curr.right.diameter) if curr.right else (0, 0)
                    curr.height = 1 + max(lh, rh)
                    curr.diameter = max(lh + rh, ld, rd)
                    curr = None

        return root.diameter


class Test(unittest.TestCase):
    def test(self):
        self._test([1, 2, 3, 4, 5], 3)

    def _test(self, root, expected):
        root = TreeNode.from_array(root)
        actual = Solution().diameterOfBinaryTree(root)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
