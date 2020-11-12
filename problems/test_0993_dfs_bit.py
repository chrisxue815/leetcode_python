import unittest

import utils
from tree import TreeNode


# O(n) time. O(log(n)) space. Recursive pre-order traversal, bit manipulation.
class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        index1 = -1
        result = False

        def dfs(curr, index):
            if not curr:
                return False

            if curr.val == x or curr.val == y:
                nonlocal index1
                if index1 == -1:
                    index1 = index
                else:
                    nonlocal result
                    result = index.bit_length() == index1.bit_length() and index != (index1 | 1)

            return dfs(curr.left, index << 1) or dfs(curr.right, (index << 1) + 1)

        dfs(root, 1)
        return result


class Test(unittest.TestCase):
    def test(self):
        cases = utils.load_test_json(__file__).test_cases

        for case in cases:
            args = str(case.args)
            root = TreeNode.from_array(case.args.root)
            actual = Solution().isCousins(root, case.args.x, case.args.y)
            self.assertEqual(case.expected, actual, msg=args)


if __name__ == '__main__':
    unittest.main()
