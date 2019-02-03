import unittest


class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        num = 0
        for ch in s:
            num = num * 26 + ord(ch) - ord('A') + 1
        return num


class Test(unittest.TestCase):
    def test(self):
        self._test('A', 1)
        self._test('B', 2)
        self._test('Z', 26)
        self._test('AA', 27)
        self._test('AB', 28)
        self._test('AZ', 52)
        self._test('BA', 53)
        self._test('BB', 54)
        self._test('BZ', 78)

    def _test(self, s, expected):
        actual = Solution().titleToNumber(s)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
