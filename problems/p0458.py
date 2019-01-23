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
        cases = utils.load_test_json(__file__).test_cases

        for case in cases:
            actual = Solution().poorPigs(**vars(case.args))
            self.assertEqual(case.expected, actual)


if __name__ == '__main__':
    unittest.main()
