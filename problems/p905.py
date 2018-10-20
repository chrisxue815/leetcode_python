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
        cases = utils.load_json_from_path('../leetcode_test_cases/p905.json').test_cases

        for case in cases:
            actual = Solution().sortArrayByParity(case.a)
            self.assertItemsEqual(case.a, actual)

            i = 0
            while i < len(actual):
                if actual[i] & 1:
                    break
                i += 1

            for i in xrange(i, len(actual)):
                self.assertEqual(1, actual[i] & 1)


if __name__ == '__main__':
    unittest.main()
