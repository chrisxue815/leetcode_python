import unittest
from tree import TreeNode


# O(n) time. O(h) space. Iterative in-order traversal.
# Optimization: self-balancing BST
class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        count = 0
        stack = []

        while root or stack:
            if root:
                stack.append(root)
                root = root.left
            else:
                root = stack.pop()
                count += 1
                if count == k:
                    return root.val
                root = root.right

        return None


class Test(unittest.TestCase):
    def test(self):
        self._test([4, 2, 6, 1, 3, 5, 7], 6, 6)

    def _test(self, root, k, expected):
        root = TreeNode.from_array(root)
        actual = Solution().kthSmallest(root, k)
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()
