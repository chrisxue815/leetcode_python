import unittest

_zero = ord('0')


def _process_mul_div(s, i, product):
    op = s[i]
    i += 1
    num = 0

    while i < len(s):
        ch = s[i]

        if ch == ' ':
            pass
        elif ch.isdigit():
            num = num * 10 + ord(ch) - _zero
        elif ch == '*' or ch == '/':
            product = _mul_div(op, product, num)
            op = ch
            num = 0
        else:
            break

        i += 1

    product = _mul_div(op, product, num)

    return product, i - 1


def _mul_div(op, num1, num2):
    if op == '*':
        return num1 * num2
    else:
        return num1 // num2


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

            if ch == ' ':
                pass
            elif ch.isdigit():
                num = num * 10 + ord(ch) - _zero
            elif ch == '+':
                sum_ += sign * num
                num = 0
                sign = 1
            elif ch == '-':
                sum_ += sign * num
                num = 0
                sign = -1
            else:
                num, i = _process_mul_div(s, i, num)

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
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()
