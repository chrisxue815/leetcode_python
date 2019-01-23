import unittest
import utils


# O(n) time. O(1) space. Two pointers.
class Solution(object):
    def sortedSquares(self, a):
        """
        :type a: List[int]
        :rtype: List[int]
        """
        result = []

        hi = 0
        while hi < len(a) and a[hi] < 0:
            hi += 1

        lo = hi - 1

        while lo >= 0 and hi < len(a):
            if a[lo] * a[lo] < a[hi] * a[hi]:
                result.append(a[lo] * a[lo])
                lo -= 1
            else:
                result.append(a[hi] * a[hi])
                hi += 1

        for lo in xrange(lo, -1, -1):
            result.append(a[lo] * a[lo])

        for hi in xrange(hi, len(a)):
            result.append(a[hi] * a[hi])

        return result


class Test(unittest.TestCase):
    def test(self):
        cases = utils.load_test_json(__file__).test_cases

        for case in cases:
            actual = Solution().sortedSquares(**vars(case.args))
            self.assertEqual(case.expected, actual)


if __name__ == '__main__':
    unittest.main()
