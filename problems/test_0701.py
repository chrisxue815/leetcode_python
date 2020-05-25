import unittest
import utils
from tree import TreeNode


# O(log(n)) time. O(log(n)) space. Recursive DFS.
class Solution(object):
    def insertIntoBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        if root:
            if val < root.val:
                root.left = self.insertIntoBST(root.left, val)
            else:
                root.right = self.insertIntoBST(root.right, val)
            return root
        else:
            return TreeNode(val)


class Test(unittest.TestCase):
    def test(self):
        cases = utils.load_test_json(__file__).test_cases

        for case in cases:
            args = str(case.args)
            root = TreeNode.from_array(case.args.root)
            actual = Solution().insertIntoBST(root, case.args.val)
            actual = actual.to_array()
            self.assertIn(actual, case.expected, msg=args)


if __name__ == '__main__':
    unittest.main()
