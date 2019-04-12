import unittest
import utils


# O(nlog(n)) time. O(1) space. Geometry, sorting.
class Solution(object):
    def largestPerimeter(self, a):
        """
        :type a: List[int]
        :rtype: int
        """
        a.sort(reverse=True)

        for i in range(2, len(a)):
            u = a[i - 2]
            v = a[i - 1]
            w = a[i]

            if u < v + w:
                return u + v + w

        return 0



class Test(unittest.TestCase):
    def test(self):
        cases = utils.load_test_json(__file__).test_cases

        for case in cases:
            actual = Solution().largestPerimeter(**case.args._asdict())
            self.assertEqual(case.expected, actual, msg=case.args)


if __name__ == '__main__':
    unittest.main()
