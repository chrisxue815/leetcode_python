import unittest
import utils
from tree import TreeNode


# O(n) time. O(log(n)) space. Recursive DFS.
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        def dfs(curr, parent_even, grandparent_even):
            if not curr:
                return 0
            curr_even = curr.val & 1 == 0
            return (curr.val if grandparent_even else 0) + \
                   dfs(curr.left, curr_even, parent_even) + \
                   dfs(curr.right, curr_even, parent_even)

        return dfs(root, False, False)


class Test(unittest.TestCase):
    def test(self):
        cases = utils.load_test_json(__file__).test_cases

        for case in cases:
            args = str(case.args)
            root = TreeNode.from_array(case.args.root)
            actual = Solution().sumEvenGrandparent(root)
            self.assertEqual(case.expected, actual, msg=args)


if __name__ == '__main__':
    unittest.main()
