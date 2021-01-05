import unittest
from typing import List

import utils


# O(n) time. O(n) space. Monotone stack.
class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        num_k = -10 ** 9 - 1
        stack = []
        for num in reversed(nums):
            if num < num_k:
                return True
            while stack and stack[-1] < num:
                num_k = stack.pop()
            stack.append(num)
        return False


class Test(unittest.TestCase):
    def test(self):
        cases = utils.load_test_json(__file__).test_cases

        for case in cases:
            args = str(case.args)
            actual = Solution().find132pattern(**case.args.__dict__)
            self.assertEqual(case.expected, actual, msg=args)


if __name__ == '__main__':
    unittest.main()
