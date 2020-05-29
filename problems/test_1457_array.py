import unittest
import utils
from tree import TreeNode


# O(n) time. O(log(n)) space. Recursive DFS, counting array.
class Solution:
    def pseudoPalindromicPaths(self, root: TreeNode) -> int:
        count = [0] * 10

        def dfs(curr):
            if not curr:
                return 0

            count[curr.val] += 1

            if curr.left or curr.right:
                result = dfs(curr.left) + dfs(curr.right)
            else:
                num_odds = sum(c & 1 for c in count)
                result = 1 if num_odds <= 1 else 0

            count[curr.val] -= 1
            return result

        return dfs(root)


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
