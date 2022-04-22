import unittest

import utils
from tree import TreeNode


# O(n) time. O(log(n)) space. Recursive pre-order DFS.
class Solution:
    def tree2str(self, root: TreeNode) -> str:
        if not root:
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

        dfs(root)
        return ''.join(result)


class Test(unittest.TestCase):
    def test(self):
        cases = utils.load_test_json(__file__).test_cases

        for case in cases:
            args = str(case.args)
            root = TreeNode.from_array(case.args.root)
            actual = Solution().tree2str(root)
            self.assertEqual(case.expected, actual, msg=args)


if __name__ == '__main__':
    unittest.main()
