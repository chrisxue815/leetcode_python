import unittest
import fractions


def _read_num(s, i):
    ch = s[i]
    if ch == '-':
        sign = -1
        i += 1
    elif ch == '+':
        sign = 1
        i += 1
    else:
        sign = 1

    num = ord(s[i]) - ord('0')

    for i in xrange(i + 1, len(s)):
        ch = s[i]
        if not ch.isdigit():
            return sign * num, i
        num = num * 10 + ord(ch) - ord('0')

    return sign * num, len(s)


class Solution(object):
    def fractionAddition(self, s):
        """
        :type s: str
        :rtype: str
        """
        n = len(s)

        num1, i = _read_num(s, 0)
        denom1, i = _read_num(s, i + 1)
        frac = fractions.Fraction(num1, denom1)

        while i < n:
            num2, i = _read_num(s, i)
            denom2, i = _read_num(s, i + 1)

            frac += fractions.Fraction(num2, denom2)

        return str(frac.numerator) + '/' + str(frac.denominator)


class Test(unittest.TestCase):
    def test(self):
        self._test('-1/2+1/2', '0/1')
        self._test('-1/2+1/2+1/3', '1/3')
        self._test('1/3-1/2', '-1/6')
        self._test('5/3+1/3', '2/1')

    def _test(self, expression, expected):
        actual = Solution().fractionAddition(expression)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
