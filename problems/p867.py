import unittest
import utils


# O(n) time. O(1) space. Iteration.
class Solution(object):
    def transpose(self, a):
        """
        :type a: List[List[int]]
        :rtype: List[List[int]]
        """
        b = [[0] * len(a) for _ in xrange(len(a[0]))]

        for i in xrange(len(b)):
            for j in xrange(len(b[0])):
                b[i][j] = a[j][i]

        return b


class Test(unittest.TestCase):
    def test(self):
        cases = utils.load_json_from_path('../leetcode_test_cases/p867.json').test_cases

        for case in cases:
            actual = Solution().transpose(case.a)
            self.assertEqual(case.expected, actual)


if __name__ == '__main__':
    unittest.main()
