import unittest

import utils
from tree import TreeNode


# O(n) time. O(log(n)) space. Iterative in-order DFS.
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        stack = []
        dummy = parent = TreeNode(0)

        while True:
            while root:
                stack.append(root)
                root = root.left

            if not stack:
                break

            root = stack.pop()
            parent.left = None
            parent.right = root
            parent = root
            root = root.right

        parent.left = None

        return dummy.right


class Test(unittest.TestCase):
    def test(self):
        cases = utils.load_test_json(__file__).test_cases

        for case in cases:
            args = str(case.args)
            root = TreeNode.from_array(case.args.root)
            actual = Solution().increasingBST(root)
            actual = actual.to_array()
            self.assertEqual(case.expected, actual, msg=args)


if __name__ == '__main__':
    unittest.main()
