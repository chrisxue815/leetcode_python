import unittest
from typing import List

import utils


# O(n) time. O(1) space. Greedy.
class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        if not nums:
            return 0

        prev = nums[0]
        i = 1

        while i < len(nums):
            if nums[i] != prev:
                break
            i += 1
        else:
            return 1

        result = 2
        inc = prev < nums[i]

        for i in range(i + 1, len(nums)):
            if inc:
                if nums[i - 1] > nums[i]:
                    result += 1
                    inc = not inc
            else:
                if nums[i - 1] < nums[i]:
                    result += 1
                    inc = not inc

        return result


class Test(unittest.TestCase):
    def test(self):
        cases = utils.load_test_json(__file__).test_cases

        for case in cases:
            actual = Solution().wiggleMaxLength(**case.args._asdict())
            self.assertEqual(case.expected, actual, case.args)


if __name__ == '__main__':
    unittest.main()
