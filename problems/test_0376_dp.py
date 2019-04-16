import unittest
from typing import List

import utils


# O(n) time. O(n) space. DP.
class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        inc = [0] * len(nums)  # inc[i]: the length of the longest wiggle subsequence in nums[:i+1] where nums[i-1] < nums[i]
        dec = [0] * len(nums)  # dec[i]: the length of the longest wiggle subsequence in nums[:i+1] where nums[i-1] > nums[i]
        inc[0] = 1
        dec[0] = 1

        for i in range(1, len(nums)):
            if nums[i - 1] < nums[i]:
                inc[i] = dec[i - 1] + 1
                dec[i] = dec[i - 1]
            elif nums[i - 1] > nums[i]:
                inc[i] = inc[i - 1]
                dec[i] = inc[i - 1] + 1
            else:
                inc[i] = inc[i - 1]
                dec[i] = dec[i - 1]

        return max(inc[-1], dec[-1])


class Test(unittest.TestCase):
    def test(self):
        cases = utils.load_test_json(__file__).test_cases

        for case in cases:
            actual = Solution().wiggleMaxLength(**case.args.__dict__)
            self.assertEqual(case.expected, actual, msg=case.args)


if __name__ == '__main__':
    unittest.main()
