import unittest


class Solution(object):
    def originalDigits(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s:
            return ''

        num_ch = [0] * 256
        digits = [0] * 10

        for ch in s:
            if ch == 'z':
                digits[0] += 1
            elif ch == 'w':
                digits[2] += 1
            elif ch == 'u':
                digits[4] += 1
                num_ch[ord('f')] -= 1
            elif ch == 'x':
                digits[6] += 1
                num_ch[ord('s')] -= 1
                num_ch[ord('i')] -= 1
            elif ch == 'g':
                digits[8] += 1
                num_ch[ord('i')] -= 1
                num_ch[ord('h')] -= 1
            else:
                num_ch[ord(ch)] += 1

        digits[3] = num_ch[ord('h')]
        digits[5] = num_ch[ord('f')]
        digits[7] = num_ch[ord('s')]

        digits[9] = num_ch[ord('i')] - digits[5]
        digits[1] = num_ch[ord('n')] - digits[7] - (digits[9] << 1)

        return ''.join(chr(digit + ord('0')) * num_digit for digit, num_digit in enumerate(digits) if num_digit)


class Test(unittest.TestCase):
    def test(self):
        self._test('owoztneoer', '012')
        self._test('fviefuro', '45')
        self._test('xsiixssix', '666')
        self._test('nine', '9')

    def _test(self, s, expected):
        actual = Solution().originalDigits(s)
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()
