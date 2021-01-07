import unittest

import utils
from tree import TreeNode


# O(n) time. O(log(n)) space. Recursive in-order traversal.
class Solution:
    def minDiffInBST(self, root: TreeNode) -> int:
        result = 0x7fff_ffff
        prev = None

        def dfs(curr):
            if not curr:
                return

            nonlocal result
            nonlocal prev

            dfs(curr.left)

            if prev is not None:
                result = min(result, curr.val - prev)
            prev = curr.val

            dfs(curr.right)

        dfs(root)

        return result


class Test(unittest.TestCase):
    def test(self):
        cases = utils.load_test_json(__file__).test_cases

        for case in cases:
            args = str(case.args)
            root = TreeNode.from_array(case.args.root)
            actual = Solution().minDiffInBST(root)
            self.assertEqual(case.expected, actual, msg=args)


if __name__ == '__main__':
    unittest.main()
