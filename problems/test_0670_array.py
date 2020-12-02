import unittest

import utils


def find_max(digits, start):
    max_digit_index = start
    max_digit = digits[start]

    for i in range(start - 1, -1, -1):
        if digits[i] >= max_digit:
            max_digit_index = i
            max_digit = digits[i]

    return max_digit_index, max_digit


# O(n) time. O(n) space. Math, array.
class Solution:
    def maximumSwap(self, num: int) -> int:
        digits = []
        q = num
        while q:
            q, r = divmod(q, 10)
            digits.append(r)

        for i in range(len(digits) - 1, 0, -1):
            if digits[i] < digits[i - 1]:
                break
        else:
            return num

        max_digit_index, max_digit = find_max(digits, i - 1)

        while i < len(digits) and digits[i] < max_digit:
            i += 1
        digits[i - 1], digits[max_digit_index] = digits[max_digit_index], digits[i - 1]

        radix = 1
        for digit in digits:
            q += digit * radix
            radix *= 10
        return q


class Test(unittest.TestCase):
    def test(self):
        cases = utils.load_test_json(__file__).test_cases

        for case in cases:
            args = str(case.args)
            actual = Solution().maximumSwap(**case.args.__dict__)
            self.assertEqual(case.expected, actual, msg=args)


if __name__ == '__main__':
    unittest.main()
