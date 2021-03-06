import unittest

import utils


# O(1) time. O(1) space. Logic.
class Solution:
    def numMovesStones(self, a, b, c):
        """
        :type a: int
        :type b: int
        :type c: int
        :rtype: List[int]
        """
        a, b, c = sorted((a, b, c))

        if a + 2 == b or b + 2 == c:
            min_ = 1
        else:
            min_ = (a + 1 < b) + (b + 1 < c)

        max_ = c - a - 2

        return [min_, max_]


class Test(unittest.TestCase):
    def test(self):
        cases = utils.load_test_json(__file__).test_cases

        for case in cases:
            args = str(case.args)
            actual = Solution().numMovesStones(**case.args.__dict__)
            self.assertEqual(case.expected, actual, msg=args)


if __name__ == '__main__':
    unittest.main()
