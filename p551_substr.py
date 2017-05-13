import unittest


class Solution(object):
    def checkRecord(self, s):
        """
        :type s: str
        :rtype: bool
        """
        return s.count('A') < 2 and s.count('LLL') == 0


class Test(unittest.TestCase):
    def test(self):
        self._test('PPALLP', True)
        self._test('PPALLL', False)

    def _test(self, s, expected):
        actual = Solution().checkRecord(s)
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()
