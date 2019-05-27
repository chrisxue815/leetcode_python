import itertools
import unittest
import utils


# O(n!) time. O(n) space. Backtracking.
class Solution:
    def largestTimeFromDigits(self, a):
        """
        :type a: List[int]
        :rtype: str
        """
        result = -1

        for p in itertools.permutations(a):
            hour = p[0] * 10 + p[1]
            minute = p[2] * 10 + p[3]

            if 0 <= hour <= 23 and 0 <= minute <= 59:
                elapsed = hour * 60 + minute
                if result < elapsed:
                    result = elapsed

        if result == -1:
            return ''
        else:
            return '{:02d}:{:02d}'.format(*divmod(result, 60))


class Test(unittest.TestCase):
    def test(self):
        cases = utils.load_test_json(__file__).test_cases

        for case in cases:
            args = str(case.args)
            actual = Solution().largestTimeFromDigits(**case.args.__dict__)
            self.assertEqual(case.expected, actual, msg=args)


if __name__ == '__main__':
    unittest.main()
