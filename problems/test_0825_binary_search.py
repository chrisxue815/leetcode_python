import bisect
import unittest
from typing import List

import utils


# O(nlog(n)) time. O(1) space. Logic, array, binary search.
class Solution:
    def numFriendRequests(self, ages: List[int]) -> int:
        result = 0
        ages.sort()
        a = 0

        while a < len(ages):
            min_age_b = ages[a] // 2 + 7
            b = bisect.bisect_right(ages, min_age_b, 0, a)

            younger = a - b
            result += younger

            c = a + 1
            while c < len(ages) and ages[c] == ages[a]:
                c += 1

            same_age = c - a
            result += younger * (same_age - 1)

            if ages[a] > ages[a] // 2 + 7:
                result += same_age * (same_age - 1)

            a = c

        return result


class Test(unittest.TestCase):
    def test(self):
        cases = utils.load_test_json(__file__).test_cases

        for case in cases:
            args = str(case.args)
            actual = Solution().numFriendRequests(**case.args.__dict__)
            self.assertEqual(case.expected, actual, msg=args)


if __name__ == '__main__':
    unittest.main()
