import unittest
import utils
from tree import TreeNode

# O(n) time. O(log(n)) space. Recursive pre-order DFS.
class Solution(object):
    def isCousins(self, root, x, y):
        """
        :type root: TreeNode
        :type x: int
        :type y: int
        :rtype: bool
        """
        found = []

        def dfs(curr, parent, depth):
            if not curr:
                return False

            if curr.val == x or curr.val == y:
                if found:
                    return parent is not found[0] and depth == found[1]
                else:
                    found[:] = [parent, depth]

            return dfs(curr.left, curr.val, depth + 1) or dfs(curr.right, curr.val, depth + 1)

        return dfs(root, None, 0)


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
