import unittest
import utils


# O(n) time. O(1) space. Iteration.
class Solution(object):
    def minDeletionSize(self, a):
        """
        :type a: List[str]
        :rtype: int
        """
        result = 0

        for j in range(len(a[0])):
            for i in range(1, len(a)):
                if a[i - 1][j] > a[i][j]:
                    result += 1
                    break

        return result


class Test(unittest.TestCase):
    def test(self):
        cases = utils.load_test_json(__file__).test_cases

        for case in cases:
            actual = Solution().minDeletionSize(**case.args._asdict())
            self.assertEqual(case.expected, actual)


if __name__ == '__main__':
    unittest.main()
