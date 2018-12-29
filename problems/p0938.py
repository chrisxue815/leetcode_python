import unittest
import utils
from tree import TreeNode


# O(n) time. O(log(n)) space. Recursive pre-order DFS.
class Solution(object):
    def rangeSumBST(self, root, l, r):
        """
        :type root: TreeNode
        :type l: int
        :type r: int
        :rtype: int
        """
        if not root:
            return 0

        if l <= root.val <= r:
            result = root.val
        else:
            result = 0

        if l <= root.val:
            result += self.rangeSumBST(root.left, l, r)

        if root.val <= r:
            result += self.rangeSumBST(root.right, l, r)

        return result


class Test(unittest.TestCase):
    def test(self):
        cases = utils.load_test_json(__file__).test_cases

        for case in cases:
            root = TreeNode.from_array(case.root)
            actual = Solution().rangeSumBST(root, case.l, case.r)
            self.assertEqual(case.expected, actual)


if __name__ == '__main__':
    unittest.main()
