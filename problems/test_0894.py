import unittest
from typing import List

import utils
from tree import TreeNode


# Backtracking.
class Solution:
    def allPossibleFBT(self, N: int) -> List[TreeNode]:
        if N < 1 or N & 1 == 0:
            return []
        if N == 1:
            return [TreeNode(0)]

        result = []

        for left_n in range(1, N - 1, 2):
            right_n = N - 1 - left_n
            left_nodes = self.allPossibleFBT(left_n)

            for left in left_nodes:
                right_nodes = self.allPossibleFBT(right_n)
                for right in right_nodes:
                    root = TreeNode(0)
                    root.left = left
                    root.right = right
                    result.append(root)

        return result


class Test(unittest.TestCase):
    def test(self):
        cases = utils.load_test_json(__file__).test_cases

        for case in cases:
            args = str(case.args)
            actual = Solution().allPossibleFBT(**case.args.__dict__)
            actual = [root.to_array() for root in actual]
            self.assertCountEqual(case.expected, actual, msg=args)


if __name__ == '__main__':
    unittest.main()
