import unittest
import utils


# O(n) time. O(1) space.
class Solution:
    def repeatedNTimes(self, a):
        """
        :type a: List[int]
        :rtype: int
        """
        for i in range(2, len(a)):
            if a[i - 2] == a[i] or a[i - 1] == a[i]:
                return a[i]

        return a[0]


class Test(unittest.TestCase):
    def test(self):
        cases = utils.load_test_json(__file__).test_cases

        for case in cases:
            args = str(case.args)
            actual = Solution().repeatedNTimes(**case.args.__dict__)
            self.assertEqual(case.expected, actual, msg=args)


if __name__ == '__main__':
    unittest.main()
