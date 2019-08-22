import unittest

import utils
from tree import TreeNode


# O(n) time. O(log(n)) space. BFS.
class Solution:
    def maxLevelSum(self, root: TreeNode) -> int:
        if not root:
            return 0

        max_sum = 0
        max_sum_level = 1
        level = 1
        q = [root]

        while q:
            s = 0
            new_q = []

            for curr in q:
                s += curr.val
                if curr.left:
                    new_q.append(curr.left)
                if curr.right:
                    new_q.append(curr.right)

            if max_sum < s:
                max_sum = s
                max_sum_level = level
            q = new_q
            level += 1

        return max_sum_level


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
