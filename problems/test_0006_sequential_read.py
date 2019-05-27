import unittest


class Solution:
    def convert(self, s, n):
        """
        :type s: str
        :type n: int
        :rtype: str
        """
        if n == 1 or n >= len(s):
            return s

        result = [''] * n

        row = 0
        step = 1

        for ch in s:
            result[row] += ch
            if row == 0:
                step = 1
            elif row == n - 1:
                step = -1
            row += step

        return ''.join(result)


class Test(unittest.TestCase):
    def test(self):
        self._test('PAYPALISHIRING', 3, 'PAHNAPLSIIGYIR')
        self._test('012345', 1, '012345')
        self._test('012345', 2, '024135')
        self._test('012345', 3, '041352')
        self._test('0123456789', 4, '0615724839')
        self._test('0123456789', 5, '0817926354')

    def _test(self, s, numRows, expected):
        actual = Solution().convert(s, numRows)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
