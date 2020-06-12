import unittest
from typing import List

import utils
from tree import TreeNode


# O(n) time. O(n) space. Recursive in-order DFS.
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        values = []

        def dfs(curr):
            if not curr:
                return
            dfs(curr.left)
            values.append(curr.val)
            dfs(curr.right)

        dfs(root)

        def reconstruct(start, end):
            if start >= end:
                return None
            mid = start + ((end - start) >> 1)
            curr = TreeNode(values[mid])
            curr.left = reconstruct(start, mid)
            curr.right = reconstruct(mid + 1, end)
            return curr

        return reconstruct(0, len(values))


class Test(unittest.TestCase):
    def test(self):
        cases = utils.load_test_json(__file__).test_cases

        for case in cases:
            args = str(case.args)
            root = TreeNode.from_array(case.args.root)
            actual = Solution().balanceBST(root)

            self.assertEqual(in_order(root), in_order(actual), msg=args)
            self.assertTrue(is_balanced(root))


def in_order(root):
    values = []

    def dfs(curr):
        if not curr:
            return
        dfs(curr.left)
        values.append(curr.val)
        dfs(curr.right)

    dfs(root)
    return values


def is_balanced(root):
    def dfs(curr):
        if not curr:
            return True, 0

        left_valid, left_height = dfs(curr.left)

        if not left_valid:
            return False, 0

        right_valid, right_height = dfs(curr.right)

        return right_valid and abs(left_height - right_height) <= 1, max(left_height, right_height)

    valid, _ = dfs(root)
    return valid


if __name__ == '__main__':
    unittest.main()
