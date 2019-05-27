import unittest
import utils
from tree import TreeNode


# O(n) time. O(log(n)) space. Iterative post-order DFS, stack.
class Solution:
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0

        stack = []
        curr = root

        while curr or stack:
            if curr:
                stack.append(curr)
                stack.append(curr)
                curr = curr.left
            else:
                curr = stack.pop()
                if stack and stack[-1] is curr:
                    curr = curr.right
                else:
                    lh, ld = (curr.left.height, curr.left.diameter) if curr.left else (0, 0)
                    rh, rd = (curr.right.height, curr.right.diameter) if curr.right else (0, 0)
                    curr.height = 1 + max(lh, rh)
                    curr.diameter = max(lh + rh, ld, rd)
                    curr = None

        return root.diameter


class Test(unittest.TestCase):
    def test(self):
        cases = utils.load_test_json(__file__).test_cases

        for case in cases:
            args = str(case.args)
            root = TreeNode.from_array(case.args.root)
            actual = Solution().diameterOfBinaryTree(root)
            self.assertEqual(case.expected, actual, msg=args)


if __name__ == '__main__':
    unittest.main()
