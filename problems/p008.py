import unittest


class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        sign = 1
        num = 0
        i = 0
        while i < len(s) and s[i] == ' ':
            i += 1

        if i == len(s):
            return 0

        if s[i] == '+':
            i += 1
        elif s[i] == '-':
            sign = -1
            i += 1

        while i < len(s) and s[i].isdigit():
            num = num * 10 + ord(s[i]) - ord('0')  # checking overflow in other languages
            i += 1

        num *= sign

        if num >= 0x7FFFFFFF:
            return 0x7FFFFFFF
        if num <= -0x80000000:
            return -0x80000000

        return num


class Test(unittest.TestCase):
    def test(self):
        self._test('1', 1)
        self._test('+1', 1)
        self._test(' +123zxc', 123)
        self._test(' -123zxc', -123)
        self._test('999999999999999', 0x7FFFFFFF)

    def _test(self, s, expected):
        actual = Solution().myAtoi(s)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
