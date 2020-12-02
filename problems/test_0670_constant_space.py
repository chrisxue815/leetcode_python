import unittest

import utils


# O(n) time. O(1) space. Math.
class Solution:
    def maximumSwap(self, num: int) -> int:
        i = 0
        pending = num
        max_digit = max_digit_index = left_digit = left_digit_index = right_digit = right_digit_index = -1

        while pending > 0:
            pending, digit = divmod(pending, 10)
            if digit > max_digit:
                max_digit = digit
                max_digit_index = i
            elif digit < max_digit:
                left_digit = digit
                left_digit_index = i
                right_digit = max_digit
                right_digit_index = max_digit_index
            i += 1

        result = 0
        multiple = 1
        i = 0
        pending = num
        while pending > 0:
            pending, digit = divmod(pending, 10)
            if i == left_digit_index:
                digit = right_digit
            elif i == right_digit_index:
                digit = left_digit
            result += multiple * digit
            multiple *= 10
            i += 1

        return result


class Test(unittest.TestCase):
    def test(self):
        cases = utils.load_test_json(__file__).test_cases

        for case in cases:
            args = str(case.args)
            actual = Solution().maximumSwap(**case.args.__dict__)
            self.assertEqual(case.expected, actual, msg=args)


if __name__ == '__main__':
    unittest.main()
