import unittest

import utils
from tree import TreeNode


class Solution:
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        return p and q and p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right) \
            or not p and not q


class Test(unittest.TestCase):
    def test(self):
        cases = utils.load_test_json(__file__).test_cases

        for case in cases:
            args = str(case.args)

            p = TreeNode.from_array(case.args.p)
            q = TreeNode.from_array(case.args.q)

            actual = Solution().isSameTree(p, q)
            self.assertEqual(case.expected, actual, msg=args)

            actual = Solution().isSameTree(q, p)
            self.assertEqual(case.expected, actual, msg=args)


if __name__ == '__main__':
    unittest.main()
