import unittest
from typing import List

import utils


# O(n) time. O(1) space. Ring detection.
class Solution:
    def arrayNesting(self, nums: List[int]) -> int:
        result = 0
        for start, num in enumerate(nums):
            if num == -1:
                continue

            size = 0
            i = start

            while nums[i] != -1:
                size += 1
                nxt = nums[i]
                nums[i] = -1
                i = nxt

            result = max(result, size)

        return result


class Test(unittest.TestCase):
    def test(self):
        cases = utils.load_test_json(__file__).test_cases

        for case in cases:
            args = str(case.args)
            actual = Solution().arrayNesting(**case.args.__dict__)
            self.assertEqual(case.expected, actual, msg=args)


if __name__ == '__main__':
    unittest.main()
