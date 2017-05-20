import unittest


class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack = []
        sign = 1
        lo = 0
        hi = 0
        result = 0
        while hi < len(s):
            ch = s[hi]

            if lo < hi and not ch.isdigit():
                num_s = s[lo:hi]
                if num_s != '-':
                    num = int(num_s)
                    result += num * sign

            if ch == '+':
                lo = hi + 1
            elif ch == '-':
                lo = hi
            elif ch == '(':
                lo = hi + 1
                stack.append(sign)
                if hi > 0 and s[hi - 1] == '-':
                    sign = -sign
            elif ch == ')':
                lo = hi + 1
                sign = stack.pop()
            elif ch == ' ':
                lo = hi + 1

            hi += 1

        if lo < hi:
            num = int(s[lo:hi])
            result += num * sign

        return result


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
