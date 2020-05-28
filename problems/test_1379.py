import unittest
import utils
from tree import TreeNode


# O(n) time. O(n) space. BFS.
class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        if not original:
            return None
        if original is target:
            return cloned
        return self.getTargetCopy(original.left, cloned.left, target) or \
               self.getTargetCopy(original.right, cloned.right, target)


class Test(unittest.TestCase):
    def test(self):
        cases = utils.load_test_json(__file__).test_cases

        for case in cases:
            args = str(case.args)
            original = TreeNode.from_array(case.args.original)
            cloned = TreeNode.from_array(case.args.original)
            target = self.find_node(original, case.args.target)
            expected = self.find_node(cloned, case.args.target)

            actual = Solution().getTargetCopy(original, cloned, target)

            self.assertEqual(expected, actual, msg=args)

    def find_node(self, root, val):
        if not root:
            return None
        if root.val == val:
            return root
        return self.find_node(root.left, val) or self.find_node(root.right, val)


if __name__ == '__main__':
    unittest.main()
