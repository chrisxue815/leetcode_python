import unittest
import utils


# O(n) time. O(n) space. DP.
class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        counts = [0] * (num + 1)

        for x in xrange(1, num + 1):
            counts[x] = counts[x >> 1] + (x & 1)

        return counts


class Test(unittest.TestCase):
    def test(self):
        cases = utils.load_json_from_path('../leetcode_test_cases/p338.json').test_cases

        for case in cases:
            actual = Solution().countBits(case.num)
            self.assertEqual(case.expected, actual)


if __name__ == '__main__':
    unittest.main()
