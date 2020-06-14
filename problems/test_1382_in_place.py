import math
import unittest
from typing import List

import utils
from tree import TreeNode


# O(n) time. O(1) space. DSW algorithm.
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        if not root:
            return None

        def tree_to_vine(tail):
            count = 0
            rest = tail.right
            while rest:
                if rest.left:
                    pivot = rest.left
                    rest.left = pivot.right
                    pivot.right = rest
                    rest = pivot
                    tail.right = pivot
                else:
                    tail = rest
                    rest = rest.right
                    count += 1
            return count

        def compress(tail, count):
            rest = tail.right
            for _ in range(count):
                pivot = rest.right
                rest.right = pivot.left
                pivot.left = rest
                tail.right = pivot
                tail = pivot
                rest = pivot.right

        dummy = TreeNode(0)
        dummy.right = root
        size = tree_to_vine(dummy)

        non_leaves = int(2 ** int(math.log(size + 1, 2))) - 1
        compress(dummy, size - non_leaves)
        non_leaves >>= 1
        while non_leaves > 0:
            compress(dummy, non_leaves)
            non_leaves >>= 1

        return dummy.right


class Test(unittest.TestCase):
    def test(self):
        cases = utils.load_test_json(__file__).test_cases

        for case in cases:
            args = str(case.args)
            root = TreeNode.from_array(case.args.root)
            expected = in_order(root)
            actual = Solution().balanceBST(root)

            self.assertEqual(expected, in_order(actual), msg=args)
            self.assertTrue(is_balanced(actual))


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

        return right_valid and abs(left_height - right_height) <= 1, max(left_height, right_height) + 1

    valid, _ = dfs(root)
    return valid


if __name__ == '__main__':
    unittest.main()
