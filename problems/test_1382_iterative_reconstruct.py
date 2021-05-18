import unittest

import utils
from tree import TreeNode


# O(n) time. O(n) space. Iterative in-order DFS.
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        nodes = []
        stack = []

        while root or stack:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            nodes.append(root)
            root = root.right

        def reconstruct(start, end):
            if start >= end:
                return None
            mid = start + ((end - start) >> 1)
            curr = nodes[mid]
            curr.left = reconstruct(start, mid)
            curr.right = reconstruct(mid + 1, end)
            return curr

        return reconstruct(0, len(nodes))


class Test(unittest.TestCase):
    def test(self):
        utils.test(self, __file__, Solution, process_case=self.process_case, check_result=self.check_result)

    def process_case(self, case):
        utils.root_array_to_tree(case.args)
        case.expected = self.in_order(case.args.root)

    def check_result(self, case, actual, msg):
        self.assertEqual(case.expected, self.in_order(actual), msg=msg)
        self.assertTrue(self.is_balanced(actual))

    def in_order(self, root):
        values = []

        def dfs(curr):
            if not curr:
                return
            dfs(curr.left)
            values.append(curr.val)
            dfs(curr.right)

        dfs(root)
        return values

    def is_balanced(self, root):
        def dfs(curr):
            if not curr:
                return True, 0

            left_valid, left_height = dfs(curr.left)

            if not left_valid:
                return False, 0

            right_valid, right_height = dfs(curr.right)

            return right_valid and abs(left_height - right_height) <= 1, max(left_height, right_height) + 1

        valid, _ = dfs(root)
        return valid


if __name__ == '__main__':
    unittest.main()
