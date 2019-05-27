import unittest
import utils
from tree import TreeNode


def dfs(root, leaves):
    if not root.left and not root.right:
        leaves.append(root.val)
    else:
        if root.left:
            dfs(root.left, leaves)
        if root.right:
            dfs(root.right, leaves)


# O(n) time. O(n) space. Recursive DFS.
class Solution:
    def leafSimilar(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """
        if not root1:
            return not root2
        if not root2:
            return False

        leaves1 = []
        leaves2 = []

        dfs(root1, leaves1)
        dfs(root2, leaves2)

        return leaves1 == leaves2


class Test(unittest.TestCase):
    def test(self):
        cases = utils.load_test_json(__file__).test_cases

        for case in cases:
            args = str(case.args)
            root1 = TreeNode.from_array(case.args.root1)
            root2 = TreeNode.from_array(case.args.root2)
            actual = Solution().leafSimilar(root1, root2)
            self.assertEqual(case.expected, actual, msg=args)


if __name__ == '__main__':
    unittest.main()
