import unittest

import utils
from tree import TreeNode


def height_and_count(root):
    if not root:
        return -1, 0

    lh, lc = height_and_count(root.left)
    if lc != (1 << (lh + 1)) - 1:
        return lh + 1, lc + (1 << lh)

    rh, rc = height_and_count(root.right)
    return lh + 1, lc + rc + 1


# O(n) time. O(log(n)) space. Tree, math, geometric progression.
class Solution:
    def countNodes(self, root: TreeNode) -> int:
        height, count = height_and_count(root)
        return count


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
