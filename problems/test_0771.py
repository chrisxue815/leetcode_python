import unittest
import utils


# O(n) time. O(n) space. Hash table.
class Solution(object):
    def numJewelsInStones(self, j, s):
        """
        :type j: str
        :type s: str
        :rtype: int
        """
        j = set(j)
        return sum(stone in j for stone in s)


class Test(unittest.TestCase):
    def test(self):
        cases = utils.load_test_json(__file__).test_cases

        for case in cases:
            actual = Solution().numJewelsInStones(**case.args._asdict())
            self.assertEqual(case.expected, actual)


if __name__ == '__main__':
    unittest.main()
