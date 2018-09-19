import unittest
import utils


# O(1) time. O(1) space. Math.
class Solution(object):
    def isRectangleOverlap(self, rec1, rec2):
        """
        :type rec1: List[int]
        :type rec2: List[int]
        :rtype: bool
        """
        return rec1[0] < rec2[2] and rec2[0] < rec1[2] and \
               rec1[1] < rec2[3] and rec2[1] < rec1[3]


class Test(unittest.TestCase):
    def test(self):
        cases = utils.load_json_from_path('../leetcode_test_cases/p836.json').test_cases

        for case in cases:
            actual = Solution().isRectangleOverlap(case.rec1, case.rec2)
            self.assertEqual(case.expected, actual)


if __name__ == '__main__':
    unittest.main()
