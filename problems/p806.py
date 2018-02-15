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
        if not s:
            return [0, 0]

        num_lines = 1
        max_width = 100
        curr_width = 0

        for ch in s:
            width = widths[ord(ch) - ord('a')]
            if curr_width + width <= max_width:
                curr_width += width
            else:
                curr_width = width
                num_lines += 1

        return [num_lines, curr_width]


class Test(unittest.TestCase):
    def test(self):
        cases = utils.load_json_from_path('../leetcode_test_cases/p806.json').test_cases

        for case in cases:
            actual = Solution().numberOfLines(case.widths, case.s)
            self.assertEqual(case.expected, actual)


if __name__ == '__main__':
    unittest.main()
