import unittest
from typing import List

import utils


# O(n) time. O(1) space. Array.
class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        num_zeros = sum(num == 0 for num in arr)

        if num_zeros == 0:
            return

        hi = len(arr) + num_zeros - 1

        for lo in range(len(arr) - 1, -1, -1):
            num = arr[lo]

            if hi < len(arr):
                arr[hi] = num
            hi -= 1

            if num == 0:
                if hi < len(arr):
                    arr[hi] = 0
                hi -= 1


class Test(unittest.TestCase):
    def test(self):
        cases = utils.load_test_json(__file__).test_cases

        for case in cases:
            Solution().duplicateZeros(**case.args._asdict())
            self.assertEqual(case.expected, case.args.arr, msg=case.args)


if __name__ == '__main__':
    unittest.main()
