import unittest
import utils
from tree import TreeNode


# O(n) time. O(log(n)) space. Iterative post-order DFS, stack.
class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
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
                    lh = curr.left.height if curr.left else 0
                    rh = curr.right.height if curr.right else 0
                    if abs(lh - rh) > 1:
                        return False
                    curr.height = max(lh, rh) + 1
                    curr = None

        return True


class Test(unittest.TestCase):
    def test(self):
        cases = utils.load_test_json(__file__).test_cases

        for case in cases:
            root = TreeNode.from_array(case.root)
            actual = Solution().isBalanced(root)
            self.assertEqual(case.expected, actual)


if __name__ == '__main__':
    unittest.main()
