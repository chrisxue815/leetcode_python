import unittest
from typing import List

import utils


def _index_of(a, x, lo, hi):
    while lo <= hi:
        mid = lo + (hi - lo) // 2
        if a[mid] < x:
            lo = mid + 1
        elif a[mid] > x:
            hi = mid - 1
        else:
            return mid

    return -1


# O(nlog(n)) time. O(1) space. Binary search.
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        for i in range(n):
            x = target - numbers[i]
            j = _index_of(numbers, x, i + 1, n - 1)
            if j != -1:
                return [i + 1, j + 1]


class Test(unittest.TestCase):
    def test(self):
        cases = utils.load_test_json(__file__).test_cases

        for case in cases:
            args = str(case.args)
            actual = Solution().twoSum(**case.args.__dict__)
            self.assertEqual(case.expected, actual, msg=args)


if __name__ == '__main__':
    unittest.main()
