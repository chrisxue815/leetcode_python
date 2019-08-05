import unittest
from typing import List

import utils


# O(n) time. O(k) space. Math, hash table.
class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        sum_to_index = {0: -1}
        s = 0

        for curr in range(len(nums)):
            s += nums[curr]
            if k:
                s %= k

            prev = sum_to_index.get(s, -2)

            if prev != -2:
                if curr - prev > 1:
                    return True
            else:
                sum_to_index[s] = curr

        return False


class Test(unittest.TestCase):
    def test(self):
        cases = utils.load_test_json(__file__).test_cases

        for case in cases:
            args = str(case.args)
            actual = Solution().checkSubarraySum(**case.args.__dict__)
            self.assertEqual(case.expected, actual, msg=args)


if __name__ == '__main__':
    unittest.main()
