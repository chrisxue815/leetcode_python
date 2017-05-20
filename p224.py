import unittest

_zero = ord('0')


class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack = []
        sum_ = 0
        sign = 1
        num = 0

        for ch in s:
            if ch.isdigit():
                num = num * 10 + ord(ch) - _zero
            elif ch == '+':
                sum_ += sign * num
                num = 0
                sign = 1
            elif ch == '-':
                sum_ += sign * num
                num = 0
                sign = -1
            elif ch == '(':
                stack.append(sum_)
                stack.append(sign)
                sum_ = 0
                sign = 1
            elif ch == ')':
                num = sum_ + sign * num
                sign = stack.pop()
                sum_ = stack.pop()

        sum_ += sign * num

        return sum_


class Test(unittest.TestCase):
    def test(self):
        self._test('1 + 1', 2)
        self._test(' 2-1 + 2 ', 3)
        self._test('(1+(4+5+2)-3)+(6+8)', 23)
        self._test('(1-(2-3))', 2)
        self._test('(1-(2-(3-4)))', -2)

    def _test(self, s, expected):
        actual = Solution().calculate(s)
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()
