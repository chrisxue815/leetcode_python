import unittest
import utils


# O(nlog(n)) time. O(1) space. Greedy.
class Solution(object):
    def smallestRangeII(self, a, k):
        """
        :type a: List[int]
        :type k: int
        :rtype: int
        """
        a.sort()
        result = a[-1] - a[0]

        for i in range(0, len(a) - 1):
            result = min(result, max(a[-1] - k, a[i] + k) - min(a[0] + k, a[i + 1] - k))

        return result


class Test(unittest.TestCase):
    def test(self):
        cases = utils.load_test_json(__file__).test_cases

        for case in cases:
            actual = Solution().smallestRangeII(**case.args._asdict())
            self.assertEqual(case.expected, actual)


if __name__ == '__main__':
    unittest.main()
