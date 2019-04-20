import unittest
import utils
from tree import TreeNode


# O(n) time. O(log(n)) space. Iterative post-order DFS, stack.
class Solution(object):
    def findTilt(self, root):
        """
        :type curr: TreeNode
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
                    left_sum, left_tilt = (curr.left.sum, curr.left.tilt) if curr.left else (0, 0)
                    right_sum, right_tilt = (curr.right.sum, curr.right.tilt) if curr.right else (0, 0)
                    curr.sum = left_sum + right_sum + curr.val
                    curr.tilt = left_tilt + right_tilt + abs(left_sum - right_sum)
                    curr = None

        return root.tilt


class Test(unittest.TestCase):
    def test(self):
        cases = utils.load_test_json(__file__).test_cases

        for case in cases:
            args = str(case.args)
            root = TreeNode.from_array(case.args.root)
            actual = Solution().findTilt(root)
            self.assertEqual(case.expected, actual, msg=args)


if __name__ == '__main__':
    unittest.main()
