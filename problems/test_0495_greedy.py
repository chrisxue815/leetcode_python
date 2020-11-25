import unittest
from typing import List

import utils


# O(n) time. O(1) space. Array.
class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        if not timeSeries:
            return 0

        result = duration
        prev = timeSeries[0]

        for curr in timeSeries:
            result += min(duration, curr - prev)
            prev = curr

        return result


class Test(unittest.TestCase):
    def test(self):
        cases = utils.load_test_json(__file__).test_cases

        for case in cases:
            args = str(case.args)
            actual = Solution().findPoisonedDuration(**case.args.__dict__)
            self.assertEqual(case.expected, actual, msg=args)


if __name__ == '__main__':
    unittest.main()
