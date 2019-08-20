import unittest
from typing import List

import utils


# O(nlog(n)) time. O(n) space. Merge sort.
class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        result = [0] * len(nums)

        def sort(dst, src, lo, hi):
            if lo + 1 >= hi:
                return

            mid = lo + ((hi - lo) >> 1)

            sort(src, dst, lo, mid)
            sort(src, dst, mid, hi)

            p = mid - 1
            q = hi - 1

            for i in range(hi - 1, lo - 1, -1):
                if q < mid or p >= lo and src[p][1] > src[q][1]:
                    result[src[p][0]] += q - mid + 1
                    dst[i] = src[p]
                    p -= 1
                else:
                    dst[i] = src[q]
                    q -= 1

        nums = list(enumerate(nums))
        aux = list(nums)

        sort(nums, aux, 0, len(nums))
        return result


class Test(unittest.TestCase):
    def test(self):
        cases = utils.load_test_json(__file__).test_cases

        for case in cases:
            args = str(case.args)
            actual = Solution().countSmaller(**case.args.__dict__)
            self.assertEqual(case.expected, actual, msg=args)


if __name__ == '__main__':
    unittest.main()
