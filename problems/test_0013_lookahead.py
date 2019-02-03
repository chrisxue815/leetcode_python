import unittest


class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        symbols = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        result = 0

        for i in range(len(s) - 1):
            curr = symbols[s[i]]
            if curr < symbols[s[i + 1]]:
                result -= curr
            else:
                result += curr

        return result + symbols[s[-1]]


class Test(unittest.TestCase):
    def test(self):
        self._test('I', 1)
        self._test('II', 2)
        self._test('III', 3)
        self._test('IV', 4)
        self._test('V', 5)
        self._test('VI', 6)
        self._test('VII', 7)
        self._test('VIII', 8)
        self._test('IX', 9)
        self._test('X', 10)
        self._test('XI', 11)
        self._test('XIV', 14)
        self._test('XV', 15)
        self._test('XVI', 16)
        self._test('XX', 20)
        self._test('XL', 40)
        self._test('XLIV', 44)
        self._test('XLV', 45)
        self._test('XLVIII', 48)
        self._test('IL', 49)

    def _test(self, s, expected):
        actual = Solution().romanToInt(s)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
