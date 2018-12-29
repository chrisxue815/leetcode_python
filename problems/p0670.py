import unittest


def find_max(digits, start):
    max_digit_index = start
    max_digit = digits[start]

    for i in xrange(start - 1, -1, -1):
        if digits[i] >= max_digit:
            max_digit_index = i
            max_digit = digits[i]

    return max_digit_index, max_digit


# O(n). Math.
class Solution(object):
    def maximumSwap(self, num):
        """
        :type num: int
        :rtype: int
        """
        digits = []
        q = num
        while q:
            q, r = divmod(q, 10)
            digits.append(r)

        for i in xrange(len(digits) - 1, 0, -1):
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
        self._test(2736, 7236)
        self._test(9973, 9973)
        self._test(31313, 33311)
        self._test(11313, 31311)

    def _test(self, n, expected):
        actual = Solution().maximumSwap(n)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
