import unittest
from typing import List

import utils


# O(n^2) time. O(1) space. Array, iteration.
class Solution:
    def numFriendRequests(self, ages: List[int]) -> int:
        def friend(a, b):
            return not (b <= 0.5 * a + 7 or b > a or b > 100 > a)

        return sum(friend(ages[a], ages[b]) + friend(ages[b], ages[a])
                   for a in range(len(ages)) for b in range(a + 1, len(ages)))


class Test(unittest.TestCase):
    def test(self):
        cases = utils.load_test_json(__file__).test_cases

        for case in cases:
            args = str(case.args)
            actual = Solution().numFriendRequests(**case.args.__dict__)
            self.assertEqual(case.expected, actual, msg=args)


if __name__ == '__main__':
    unittest.main()
