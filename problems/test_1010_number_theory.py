import unittest

import utils


# O(n) time. O(n) space. Number theory, array.
class Solution:
    def numPairsDivisibleBy60(self, time):
        """
        :type time: List[int]
        :rtype: int
        """
        count = [0] * 60

        for t in time:
            count[t % 60] += 1

        result = count[0] * (count[0] - 1) // 2 + count[30] * (count[30] - 1) // 2

        for t in range(1, 30):
            result += count[t] * count[60 - t]

        return result


class Test(unittest.TestCase):
    def test(self):
        cases = utils.load_test_json(__file__).test_cases

        for case in cases:
            args = str(case.args)
            actual = Solution().numPairsDivisibleBy60(**case.args.__dict__)
            self.assertEqual(case.expected, actual, msg=args)


if __name__ == '__main__':
    unittest.main()
