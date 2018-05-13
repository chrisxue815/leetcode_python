import unittest
import utils


# O(n) time. O(1) space. Iteration.
class Solution(object):
    def numberOfArithmeticSlices(self, a):
        """
        :type a: List[int]
        :rtype: int
        """
        result = 0
        i = 1

        while i < len(a):
            start = i
            diff = a[i] - a[i - 1]
            i += 1
            while i < len(a) and a[i] - a[i - 1] == diff:
                i += 1
            length = i - start - 1
            result += (1 + length) * length // 2

        return result


class Test(unittest.TestCase):
    def test(self):
        cases = utils.load_json_from_path('../leetcode_test_cases/p413.json').test_cases

        for case in cases:
            actual = Solution().numberOfArithmeticSlices(case.a)
            self.assertEqual(case.expected, actual)


if __name__ == '__main__':
    unittest.main()
