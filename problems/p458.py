import math
import unittest
import utils


# O(1) time. O(1) space. Math.
class Solution(object):
    def poorPigs(self, buckets, minutesToDie, minutesToTest):
        """
        :type buckets: int
        :type minutesToDie: int
        :type minutesToTest: int
        :rtype: int
        """
        return int(math.ceil(math.log(buckets, minutesToTest // minutesToDie + 1)))


class Test(unittest.TestCase):
    def test(self):
        cases = utils.load_json_from_path('../leetcode_test_cases/p458.json').test_cases

        for case in cases:
            actual = Solution().poorPigs(case.buckets, case.minutesToDie, case.minutesToTest)
            self.assertEqual(case.expected, actual)


if __name__ == '__main__':
    unittest.main()
