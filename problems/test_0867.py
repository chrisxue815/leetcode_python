import unittest
import utils


# O(n) time. O(1) space. Iteration.
class Solution(object):
    def transpose(self, a):
        """
        :type a: List[List[int]]
        :rtype: List[List[int]]
        """
        b = [[0] * len(a) for _ in range(len(a[0]))]

        for i in range(len(b)):
            for j in range(len(b[0])):
                b[i][j] = a[j][i]

        return b


class Test(unittest.TestCase):
    def test(self):
        cases = utils.load_test_json(__file__).test_cases

        for case in cases:
            actual = Solution().transpose(**case.args._asdict())
            self.assertEqual(case.expected, actual, msg=case.args)


if __name__ == '__main__':
    unittest.main()
