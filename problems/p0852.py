import unittest
import utils


# O(n) time. O(1) space. Iteration.
class Solution(object):
    def peakIndexInMountainArray(self, a):
        """
        :type a: List[int]
        :rtype: int
        """
        for i in xrange(len(a) - 1):
            if a[i] > a[i + 1]:
                return i


class Test(unittest.TestCase):
    def test(self):
        cases = utils.load_test_json(__file__).test_cases

        for case in cases:
            actual = Solution().peakIndexInMountainArray(case.a)
            self.assertEqual(case.expected, actual)


if __name__ == '__main__':
    unittest.main()
