import unittest
import utils


# O(n) time. O(1) space. Math.
class Solution(object):
    def smallestRangeI(self, a, k):
        """
        :type a: List[int]
        :type k: int
        :rtype: int
        """
        return max(0, max(a) - min(a) - 2 * k)


class Test(unittest.TestCase):
    def test(self):
        cases = utils.load_json_from_path('../leetcode_test_cases/p908.json').test_cases

        for case in cases:
            actual = Solution().smallestRangeI(case.a, case.k)
            self.assertEqual(case.expected, actual)


if __name__ == '__main__':
    unittest.main()
