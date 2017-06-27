import unittest
from tree import TreeNode


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
                if curr.right:
                    stack.append(curr.right)
                stack.append(curr)
                curr = curr.left
            else:
                curr = stack.pop()
                if stack and stack[-1] is curr.right:
                    stack[-1] = curr
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
        self._test([1, 2, 3], 1)

    def _test(self, vals, expected):
        root = TreeNode.from_array(vals)
        actual = Solution().findTilt(root)
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()
