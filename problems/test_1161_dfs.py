import unittest

import numpy as np

import utils
from tree import TreeNode


# O(n) time. O(log(n)) space. Recursive pre-order DFS.
class Solution:
    def maxLevelSum(self, root: TreeNode) -> int:
        sums = [0]

        def dfs(curr, level):
            if not curr:
                return

            if level < len(sums):
                sums[level] += curr.val
            else:
                sums.append(curr.val)

            dfs(curr.left, level + 1)
            dfs(curr.right, level + 1)

        dfs(root, 1)
        return np.argmax(sums)


class Test(unittest.TestCase):
    def test(self):
        cases = utils.load_test_json(__file__).test_cases

        for case in cases:
            args = str(case.args)
            root = TreeNode.from_array(case.args.root)
            actual = Solution().maxLevelSum(root)
            self.assertEqual(case.expected, actual, msg=args)


if __name__ == '__main__':
    unittest.main()
