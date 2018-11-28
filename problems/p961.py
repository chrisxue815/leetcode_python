import unittest
import utils


# O(n) time. O(1) space.
class Solution(object):
    def repeatedNTimes(self, a):
        """
        :type a: List[int]
        :rtype: int
        """
        for i in xrange(2, len(a)):
            if a[i - 2] == a[i] or a[i - 1] == a[i]:
                return a[i]

        return a[0]


class Test(unittest.TestCase):
    def test(self):
        cases = utils.load_json_from_path('../leetcode_test_cases/p961.json').test_cases

        for case in cases:
            actual = Solution().repeatedNTimes(case.a)
            self.assertEqual(case.expected, actual)


if __name__ == '__main__':
    unittest.main()
