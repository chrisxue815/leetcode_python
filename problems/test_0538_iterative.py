import unittest
from tree import TreeNode


class Solution:
    def convertBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        stack = []
        sum_ = 0
        curr = root
        while curr or stack:
            if curr:
                stack.append(curr)
                curr = curr.right
            else:
                curr = stack.pop()
                sum_ += curr.val
                curr.val = sum_
                curr = curr.left
        return root


class Test(unittest.TestCase):
    def test_serialize(self):
        self._test([5, 2, 13], [18, 20, 13])

    def _test(self, vals, expected):
        root = TreeNode.from_array(vals)
        actual = Solution().convertBST(root)
        actual = actual.to_array()
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
