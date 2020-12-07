import unittest
from typing import List

import utils
from tree import TreeNode


# O(n) time. O(1) space. Array.
class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        result = 0
        bound = 0

        for i, num in enumerate(arr):
            if bound < num:
                bound = num
            if i == bound:
                result += 1

        return result


class Test(unittest.TestCase):
    def test(self):
        cases = utils.load_test_json(__file__).test_cases

        for case in cases:
            args = str(case.args)
            actual = Solution().maxChunksToSorted(**case.args.__dict__)
            self.assertEqual(case.expected, actual, msg=args)


if __name__ == '__main__':
    unittest.main()
