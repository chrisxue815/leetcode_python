import unittest
import utils
from tree import TreeNode


def next_leaf(root, stack):
    while True:
        while root:
            if root.left or root.right:
                stack.append(root)
                root = root.left
            else:
                return root

        if not stack:
            return None

        root = stack.pop()
        root = root.right


# O(n) time. O(log(n)) space. Iterative DFS.
class Solution(object):
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

        stack1 = []
        stack2 = []

        while True:
            root1 = next_leaf(root1, stack1)
            root2 = next_leaf(root2, stack2)

            if not root1 or not root2:
                return not root1 and not root2

            if root1.val != root2.val:
                return False

            root1 = None
            root2 = None


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
