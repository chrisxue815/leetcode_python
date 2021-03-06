import unittest
import utils


# O(n) time. O(1) space. Math.
class Solution:
    def smallestRangeI(self, a, k):
        """
        :type a: List[int]
        :type k: int
        :rtype: int
        """
        return max(0, max(a) - min(a) - 2 * k)


class Test(unittest.TestCase):
    def test(self):
        cases = utils.load_test_json(__file__).test_cases

        for case in cases:
            args = str(case.args)
            actual = Solution().smallestRangeI(**case.args.__dict__)
            self.assertEqual(case.expected, actual, msg=args)


if __name__ == '__main__':
    unittest.main()
