import unittest

import utils
from tree import TreeNode


# O(n) time. O(log(n)) space. Recursive pre-order DFS.
class Solution:
    def findBottomLeftValue(self, root: TreeNode) -> int:
        result = 0
        max_depth = 0

        def dfs(curr, depth):
            if not curr:
                return

            nonlocal max_depth
            if max_depth < depth:
                max_depth = depth
                nonlocal result
                result = curr.val

            dfs(curr.left, depth + 1)
            dfs(curr.right, depth + 1)

        dfs(root, 1)
        return result


class Test(unittest.TestCase):
    def test(self):
        cases = utils.load_test_json(__file__).test_cases

        for case in cases:
            args = str(case.args)
            root = TreeNode.from_array(case.args.root)
            actual = Solution().findBottomLeftValue(root)
            self.assertEqual(case.expected, actual, msg=args)


if __name__ == '__main__':
    unittest.main()
