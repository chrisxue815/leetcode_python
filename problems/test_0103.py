import unittest
from tree import TreeNode, null


class Solution(object):

    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []

        vals = []
        stack = []
        stack.append(root)
        direction = 1

        while True:
            size = len(stack)
            if size == 0:
                break

            level_stack = []
            level_vals = []

            for _ in range(size):
                node = stack.pop()
                level_vals.append(node.val)

                if direction == 1:
                    left, right = node.left, node.right
                else:
                    left, right = node.right, node.left

                if left:
                    level_stack.append(left)
                if right:
                    level_stack.append(right)

            vals.append(level_vals)
            stack = level_stack
            direction = -direction

        return vals


class Test(unittest.TestCase):

    def test(self):
        self._test([3, 9, 20, null, null, 15, 7],
                   [[3], [20, 9], [15, 7]])

    def _test(self, vals, expected):
        root = TreeNode.from_array(vals)
        self.assertEqual(expected, Solution().zigzagLevelOrder(root))


if __name__ == '__main__':
    unittest.main()
