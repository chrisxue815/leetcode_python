import unittest
import utils
from tree import TreeNode


# O(n) time. O(log(n)) space. Recursive DFS.
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(curr, max_):
            if not curr:
                return 0
            if curr.val >= max_:
                good = 1
                max_ = curr.val
            else:
                good = 0
            return good + dfs(curr.left, max_) + dfs(curr.right, max_)

        return dfs(root, -10000)


class Test(unittest.TestCase):
    def test(self):
        cases = utils.load_test_json(__file__).test_cases

        for case in cases:
            args = str(case.args)
            root = TreeNode.from_array(case.args.root)
            actual = Solution().goodNodes(root)
            self.assertEqual(case.expected, actual, msg=args)


if __name__ == '__main__':
    unittest.main()
