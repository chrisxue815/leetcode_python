import unittest
import utils


# O(n) time. O(1) space. Array.
class Solution(object):
    def flipAndInvertImage(self, a):
        """
        :type a: List[List[int]]
        :rtype: List[List[int]]
        """
        for row in a:
            lo = 0
            hi = len(row) - 1
            while lo <= hi:
                row[lo], row[hi] = 1 - row[hi], 1 - row[lo]
                lo += 1
                hi -= 1

        return a


class Test(unittest.TestCase):
    def test(self):
        cases = utils.load_test_json(__file__).test_cases

        for case in cases:
            actual = Solution().flipAndInvertImage(**vars(case.args))
            self.assertEqual(case.expected, actual)


if __name__ == '__main__':
    unittest.main()
