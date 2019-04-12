import itertools
import unittest

import utils


# O(n^2) time. O(n) space. Brute-force, combination, backtracking.
class Solution(object):
    def numPairsDivisibleBy60(self, time):
        """
        :type time: List[int]
        :rtype: int
        """
        return sum((a + b) % 60 == 0 for a, b in itertools.combinations(time, 2))


class Test(unittest.TestCase):
    def test(self):
        cases = utils.load_test_json(__file__).test_cases

        for case in cases:
            actual = Solution().numPairsDivisibleBy60(**case.args._asdict())
            self.assertEqual(case.expected, actual, msg=case.args)


if __name__ == '__main__':
    unittest.main()
