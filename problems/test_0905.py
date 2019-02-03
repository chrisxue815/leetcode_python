import unittest
import utils


# O(n) time. O(1) space. Two pointers.
class Solution(object):
    def sortArrayByParity(self, a):
        """
        :type a: List[int]
        :rtype: List[int]
        """
        lo = 0
        hi = len(a) - 1

        while True:
            while lo < len(a) and a[lo] & 1 == 0:
                lo += 1

            while hi >= 0 and a[hi] & 1 == 1:
                hi -= 1

            if lo >= hi:
                break

            a[lo], a[hi] = a[hi], a[lo]
            lo += 1
            hi -= 1

        return a


class Test(unittest.TestCase):
    def test(self):
        cases = utils.load_test_json(__file__).test_cases

        for case in cases:
            actual = Solution().sortArrayByParity(**vars(case.args))
            self.assertItemsEqual(case.args.a, actual)

            i = 0
            while i < len(actual) and actual[i] & 1 == 0:
                i += 1

            for i in range(i, len(actual)):
                self.assertEqual(1, actual[i] & 1)


if __name__ == '__main__':
    unittest.main()
