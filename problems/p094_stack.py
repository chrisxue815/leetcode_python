import unittest
from tree import TreeNode


class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        result = []
        stack = []
        curr = root

        while curr or stack:
            if curr:
                stack.append(curr)
                curr = curr.left
            else:
                curr = stack.pop()
                result.append(curr.val)
                curr = curr.right

        return result


class Test(unittest.TestCase):
    def test(self):
        self._test([1, 2, 3, 4, 5, 6, 7], [4, 2, 5, 1, 6, 3, 7])

    def _test(self, root, expected):
        root = TreeNode.from_array(root)
        actual = Solution().inorderTraversal(root)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
