import unittest


class Solution(object):
    def convert(self, s, n):
        """
        :type s: str
        :type n: int
        :rtype: str
        """
        if n == 1:
            return s

        result = []

        i = 0
        while i < len(s):
            result.append(s[i])
            i += (n << 1) - 2

        for row in xrange(1, n - 1):
            i = row
            while i < len(s):
                result.append(s[i])
                i += (n - row - 1) << 1
                if i < len(s):
                    result.append(s[i])
                else:
                    break
                i += row << 1

        i = n - 1
        while i < len(s):
            result.append(s[i])
            i += (n << 1) - 2

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
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()
