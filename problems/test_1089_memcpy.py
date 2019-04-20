import unittest
from typing import List

import utils


# O(n) time. O(1) space. Array.
class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        num_zeros = 0
        lo = 0
        hi = len(arr)

        while lo < hi:
            if arr[lo] == 0:
                num_zeros += 1
                hi -= 1
            lo += 1

        half_out = hi + 1 == lo
        if half_out:
            num_zeros -= 1

        lo = len(arr) - 1 - num_zeros
        hi = lo + 1
        write_hi = len(arr)

        for lo in range(lo, -1, -1):
            if arr[lo]:
                continue

            write_lo = write_hi - hi + lo
            arr[write_lo:write_hi] = arr[lo:hi]
            hi = lo

            if half_out:
                write_hi = write_lo
                half_out = False
            else:
                write_hi = write_lo - 1
                arr[write_hi] = 0


class Test(unittest.TestCase):
    def test(self):
        cases = utils.load_test_json(__file__).test_cases

        for case in cases:
            args = str(case.args)
            Solution().duplicateZeros(**case.args.__dict__)
            self.assertEqual(case.expected, case.args.arr, msg=args)


if __name__ == '__main__':
    unittest.main()
