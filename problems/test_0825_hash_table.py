import collections
import unittest
from typing import List

import utils


# O(n + len(unique ages)^2) time. O(n) space. Hash table.
class Solution:
    def numFriendRequests(self, ages: List[int]) -> int:
        def friend(a, b):
            return not (b <= 0.5 * a + 7 or b > a or b > 100 > a)

        counts = collections.Counter(ages)

        return sum(a_count * b_count if a != b else a_count * (a_count - 1)
                   for a, a_count in counts.items() for b, b_count in counts.items() if friend(a, b))


class Test(unittest.TestCase):
    def test(self):
        cases = utils.load_test_json(__file__).test_cases

        for case in cases:
            args = str(case.args)
            actual = Solution().numFriendRequests(**case.args.__dict__)
            self.assertEqual(case.expected, actual, msg=args)


if __name__ == '__main__':
    unittest.main()
