import unittest

import utils
from tree import TreeNode


# O(n) time. O(log(n)) space. Recursive pre-order DFS.
class Solution:
    def tree2str(self, t: TreeNode) -> str:
        if not t:
            return ''

        result = []

        def dfs(curr):
            result.append(str(curr.val))

            if curr.left:
                result.append('(')
                dfs(curr.left)
                result.append(')')
            elif curr.right:
                result.append('()')

            if curr.right:
                result.append('(')
                dfs(curr.right)
                result.append(')')

        dfs(t)
        return ''.join(result)


class Test(unittest.TestCase):
    def test(self):
        cases = utils.load_test_json(__file__).test_cases

        for case in cases:
            args = str(case.args)
            t = TreeNode.from_array(case.args.t)
            actual = Solution().tree2str(t)
            self.assertEqual(case.expected, actual, msg=args)


if __name__ == '__main__':
    unittest.main()
