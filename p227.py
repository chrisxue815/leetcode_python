import unittest

_zero = ord('0')


def scan_int(s, i):
    num = 0
    while i < len(s):
        ch = s[i]
        if ch.isdigit():
            num = num * 10 + ord(ch) - _zero
        elif ch != ' ':
            break
        i += 1
    return i - 1, num


class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        sum_ = 0
        sign = 1
        num = 0
        i = 0

        while i < len(s):
            ch = s[i]

            if ch.isdigit():
                num = num * 10 + ord(ch) - _zero
            elif ch == '+' or ch == '-':
                sum_ += sign * num
                num = 0
                sign = 44 - ord(ch)
            elif ch == '*':
                i, operand = scan_int(s, i + 1)
                num *= operand
            elif ch == '/':
                i, operand = scan_int(s, i + 1)
                num //= operand

            i += 1

        sum_ += sign * num

        return sum_


class Test(unittest.TestCase):
    def test(self):
        self._test('3+2*2', 7)
        self._test(' 3/2 ', 1)
        self._test(' 3+5 / 2 ', 5)
        self._test(' 1 ', 1)
        self._test(' 5/ 2 -1 ', 1)
        self._test(' 1- 5/ 2', -1)
        self._test('1-5/2*2+7*2/4-1', -1)
        self._test('2*3', 6)
        self._test('5/2', 2)

    def _test(self, s, expected):
        actual = Solution().calculate(s)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
