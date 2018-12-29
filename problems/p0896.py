import unittest
import utils


# O(n) time. O(1) space. Iteration.
class Solution(object):
    def isMonotonic(self, a):
        """
        :type a: List[int]
        :rtype: bool
        """
        increasing = None

        for i in xrange(len(a) - 1):
            if a[i] < a[i + 1]:
                if increasing is None:
                    increasing = True
                elif not increasing:
                    return False
            elif a[i] > a[i + 1]:
                if increasing is None:
                    increasing = False
                elif increasing:
                    return False

        return True


class Test(unittest.TestCase):
    def test(self):
        cases = utils.load_test_json(__file__).test_cases

        for case in cases:
            actual = Solution().isMonotonic(case.a)
            self.assertEqual(case.expected, actual)


if __name__ == '__main__':
    unittest.main()
