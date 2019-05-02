import unittest

import utils
from tree import TreeNode


# O(log(n)) time. O(1) space. Iterative pre-order DFS.
class Solution(object):
    def closestValue(self, root: TreeNode, target: float) -> float:
        result = 0

        while root:
            if abs(result - target) > abs(root.val - target):
                result = root.val
            if target < root.val:
                root = root.left
            else:
                root = root.right

        return result


class Test(unittest.TestCase):
    def test(self):
        cases = utils.load_test_json(__file__).test_cases

        for case in cases:
            args = str(case.args)
            root = TreeNode.from_array(case.args.root)
            actual = Solution().closestValue(root, case.args.target)
            self.assertEqual(case.expected, actual, msg=args)


if __name__ == '__main__':
    unittest.main()
