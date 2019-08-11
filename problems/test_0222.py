import unittest

import utils
from tree import TreeNode


# Number of edges
def height(root):
    result = -1
    while root:
        result += 1
        root = root.left
    return result


# O(n) time. O(log(n)) space. Tree, binary search, math, geometric progression.
class Solution:
    def countNodes(self, root: TreeNode) -> int:
        tree_height = height(root)

        if tree_height == -1:
            return 0
        if tree_height == 0:
            return 1

        left_height = tree_height - 1
        right_height = height(root.right)

        if left_height == right_height:
            return (1 << (left_height + 1)) + self.countNodes(root.right)
        else:
            return (1 << (right_height + 1)) + self.countNodes(root.left)


class Test(unittest.TestCase):
    def test(self):
        cases = utils.load_test_json(__file__).test_cases

        for case in cases:
            args = str(case.args)
            root = TreeNode.from_array(case.args.root)
            actual = Solution().countNodes(root)
            self.assertEqual(len(case.args.root), actual, msg=args)


if __name__ == '__main__':
    unittest.main()
