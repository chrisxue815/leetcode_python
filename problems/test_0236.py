import unittest

import utils
from tree import TreeNode


# O(n) time. O(log(n)) space. In-order DFS.
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def dfs(curr):
            if not curr:
                return None, 0

            ancestor, num_matches_left = dfs(curr.left)
            if num_matches_left == 2:
                return ancestor, 2

            if curr is p or curr is q:
                if num_matches_left == 1:
                    return curr, 2
                else:
                    num_matches_left = 1

            ancestor, num_matches_right = dfs(curr.right)
            if num_matches_left + num_matches_right == 2:
                return ancestor or curr, 2

            return None, num_matches_left + num_matches_right

        return dfs(root)[0]


class Test(unittest.TestCase):
    def test(self):
        cases = utils.load_test_json(__file__).test_cases

        for case in cases:
            args = str(case.args)
            root = TreeNode.from_array(case.args.root)
            p = self.find_node(root, case.args.p)
            q = self.find_node(root, case.args.q)

            actual = Solution().lowestCommonAncestor(root, p, q)

            self.assertEqual(case.expected, actual.val, msg=args)

    def find_node(self, root, val):
        if not root:
            return None
        if root.val == val:
            return root
        return self.find_node(root.left, val) or self.find_node(root.right, val)


if __name__ == '__main__':
    unittest.main()
