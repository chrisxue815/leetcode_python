import unittest

import utils
from tree import TreeNode


# O(n) time. O(log(n)) space. Recursive post-order DFS.
class Solution(object):
    def sumRootToLeaf(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        def dfs(curr, num):
            if not curr:
                return 0

            num = (num << 1) | curr.val

            if curr.left or curr.right:
                return dfs(curr.left, num) + dfs(curr.right, num)
            else:
                return num

        return dfs(root, 0)


class Test(unittest.TestCase):
    def test(self):
        cases = utils.load_test_json(__file__).test_cases

        for case in cases:
            args = str(case.args)
            root = TreeNode.from_array(case.args.root)
            actual = Solution().sumRootToLeaf(root)
            self.assertEqual(case.expected, actual, msg=args)


if __name__ == '__main__':
    unittest.main()
