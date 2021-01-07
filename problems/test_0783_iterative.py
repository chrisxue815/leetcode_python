import unittest

import utils
from tree import TreeNode


# O(n) time. O(log(n)) space. Iterative in-order traversal.
class Solution:
    def minDiffInBST(self, root: TreeNode) -> int:
        if not root:
            return 0

        result = 0x7fff_ffff
        stack = []

        while root.left:
            stack.append(root)
            root = root.left

        prev = root.val
        root = root.right

        while True:
            while root:
                stack.append(root)
                root = root.left

            if not stack:
                break

            root = stack.pop()
            result = min(result, root.val - prev)
            prev = root.val
            root = root.right

        return result


class Test(unittest.TestCase):
    def test(self):
        cases = utils.load_test_json(__file__).test_cases

        for case in cases:
            args = str(case.args)
            root = TreeNode.from_array(case.args.root)
            actual = Solution().minDiffInBST(root)
            self.assertEqual(case.expected, actual, msg=args)


if __name__ == '__main__':
    unittest.main()
