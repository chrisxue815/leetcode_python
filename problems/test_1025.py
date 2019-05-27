import unittest

import utils


# O(1) time. O(1) space. Number theory, mathematical induction.
class Solution:
    def divisorGame(self, N):
        """
        :type N: int
        :rtype: bool
        """
        return N & 1 == 0


class Test(unittest.TestCase):
    def test(self):
        cases = utils.load_test_json(__file__).test_cases

        for case in cases:
            args = str(case.args)
            actual = Solution().divisorGame(**case.args.__dict__)
            self.assertEqual(case.expected, actual, msg=args)


if __name__ == '__main__':
    unittest.main()
