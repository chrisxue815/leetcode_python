import unittest
import utils


# O(n) time. O(1) space. Iteration.
class Solution(object):
    def numberOfLines(self, widths, s):
        """
        :type widths: List[int]
        :type s: str
        :rtype: List[int]
        """
        num_lines = 1
        max_width = 100
        remaining_width = max_width

        for ch in s:
            width = widths[ord(ch) - ord('a')]
            remaining_width -= width

            if remaining_width < 0:
                remaining_width = max_width - width
                num_lines += 1

        return [num_lines, max_width - remaining_width]


class Test(unittest.TestCase):
    def test(self):
        cases = utils.load_test_json(__file__).test_cases

        for case in cases:
            actual = Solution().numberOfLines(case.widths, case.s)
            self.assertEqual(case.expected, actual)


if __name__ == '__main__':
    unittest.main()
