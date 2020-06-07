import unittest
from typing import List

import utils
from tree import TreeNode


# O(n) time. O(log(n)) space. Recursive post-order DFS.
class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        result = []

        def dfs(curr):
            if not curr:
                return
            dfs(curr.left)
            dfs(curr.right)
            result.append(curr.val)

        dfs(root)

        return result


class Test(unittest.TestCase):
    def test(self):
        cases = utils.load_test_json(__file__).test_cases

        for case in cases:
            args = str(case.args)
            root = TreeNode.from_array(case.args.root)
            actual = Solution().postorderTraversal(root)
            self.assertEqual(case.expected, actual, msg=args)


if __name__ == '__main__':
    unittest.main()
