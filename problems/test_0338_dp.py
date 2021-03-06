import unittest
import utils


# O(n) time. O(n) space. DP.
class Solution:
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        counts = [0] * (num + 1)

        for x in range(1, num + 1):
            counts[x] = counts[x >> 1] + (x & 1)

        return counts


class Test(unittest.TestCase):
    def test(self):
        cases = utils.load_test_json(__file__).test_cases

        for case in cases:
            args = str(case.args)
            actual = Solution().countBits(**case.args.__dict__)
            self.assertEqual(case.expected, actual, msg=args)


if __name__ == '__main__':
    unittest.main()
