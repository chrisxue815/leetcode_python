import math
import unittest
import utils


# O(n) time. O(1) space. Iteration.
class Solution(object):
    def largeGroupPositions(self, s):
        """
        :type s: str
        :rtype: List[List[int]]
        """
        result = []
        lo = 0

        for hi in xrange(1, len(s)):
            if s[hi] != s[lo]:
                if hi - lo >= 3:
                    result.append([lo, hi - 1])
                lo = hi

        if len(s) - lo >= 3:
            result.append([lo, len(s) - 1])

        return result


class Test(unittest.TestCase):
    def test(self):
        cases = utils.load_json_from_path('../leetcode_test_cases/p830.json').test_cases

        for case in cases:
            actual = Solution().largeGroupPositions(case.s)
            self.assertEqual(case.expected, actual)


if __name__ == '__main__':
    unittest.main()
