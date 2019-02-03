import unittest
import utils
from tree import TreeNode


# O(log(n)) time. O(1) space. Tail-call optimized recursive pre-order DFS.
class Solution(object):
    def searchBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        while True:
            if not root:
                return None
            if root.val == val:
                return root
            elif root.val > val:
                root = root.left
            else:
                root = root.right


class Test(unittest.TestCase):
    def test(self):
        cases = utils.load_test_json(__file__).test_cases

        for case in cases:
            root = TreeNode.from_array(case.args.root)
            actual = Solution().searchBST(root, case.args.val)
            actual = actual.to_array()
            self.assertEqual(case.expected, actual)


if __name__ == '__main__':
    unittest.main()
