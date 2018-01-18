import unittest


class Solution(object):
    def originalDigits(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s:
            return ''

        digits = [0] * 10

        for ch in s:
            if ch == 'z':
                digits[0] += 1
            elif ch == 'n':
                digits[1] += 1
            elif ch == 'w':
                digits[2] += 1
            elif ch == 'h':
                digits[3] += 1
            elif ch == 'u':
                digits[4] += 1
            elif ch == 'f':
                digits[5] += 1
            elif ch == 'x':
                digits[6] += 1
            elif ch == 's':
                digits[7] += 1
            elif ch == 'g':
                digits[8] += 1
            elif ch == 'i':
                digits[9] += 1

        digits[3] -= digits[8]
        digits[5] -= digits[4]
        digits[7] -= digits[6]

        digits[9] -= digits[5] + digits[6] + digits[8]
        digits[1] -= digits[7] + (digits[9] << 1)

        return ''.join(chr(digit + ord('0')) * num_digit for digit, num_digit in enumerate(digits) if num_digit)


class Test(unittest.TestCase):
    def test(self):
        self._test('owoztneoer', '012')
        self._test('fviefuro', '45')
        self._test('xsiixssix', '666')
        self._test('nine', '9')

    def _test(self, s, expected):
        actual = Solution().originalDigits(s)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
