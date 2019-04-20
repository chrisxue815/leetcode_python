import unittest
import utils
from tree import TreeNode


# O(n) time. O(log(n)) space. Iterative in-order traversal.
class Solution(object):
    def minDiffInBST(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        min_diff = 0x7FFFFFFF
        prev = None
        stack = []

        while root or stack:
            if root:
                stack.append(root)
                root = root.left
            else:
                root = stack.pop()

                if prev is not None:
                    min_diff = min(min_diff, root.val - prev)
                prev = root.val

                root = root.right

        return min_diff


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
