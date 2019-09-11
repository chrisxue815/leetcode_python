import unittest

import utils
from tree import TreeNode


# O(n) time. O(log(n)) space. Recursive post-order DFS, tree height.
class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        result = 0

        # Number of nodes
        def height(curr):
            if not curr:
                return 0

            left_level = height(curr.left)
            right_level = height(curr.right)

            nonlocal result
            result = max(result, left_level + right_level)

            return max(left_level, right_level) + 1

        height(root)

        return result


class Test(unittest.TestCase):
    def test(self):
        cases = utils.load_test_json(__file__).test_cases

        for case in cases:
            args = str(case.args)
            root = TreeNode.from_array(case.args.root)
            actual = Solution().diameterOfBinaryTree(root)
            self.assertEqual(case.expected, actual, msg=args)


if __name__ == '__main__':
    unittest.main()
