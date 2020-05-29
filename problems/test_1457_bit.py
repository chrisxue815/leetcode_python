import unittest
import utils
from tree import TreeNode


# O(n) time. O(log(n)) space. Recursive DFS, bit manipulation.
class Solution:
    def pseudoPalindromicPaths(self, root: TreeNode) -> int:
        def dfs(curr, count):
            if not curr:
                return 0

            count ^= 1 << curr.val

            if curr.left or curr.right:
                result = dfs(curr.left, count) + dfs(curr.right, count)
            else:
                result = 1 if count == 0 or count & (count - 1) == 0 else 0

            return result

        return dfs(root, 0)


class Test(unittest.TestCase):
    def test(self):
        cases = utils.load_test_json(__file__).test_cases

        for case in cases:
            args = str(case.args)
            root = TreeNode.from_array(case.args.root)
            actual = Solution().pseudoPalindromicPaths(root)
            self.assertEqual(case.expected, actual, msg=args)


if __name__ == '__main__':
    unittest.main()
