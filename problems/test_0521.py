import unittest


class Solution:
    def findLUSlength(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: int
        """
        na = len(a)
        nb = len(b)

        if na > nb:
            return na
        elif na < nb:
            return nb
        elif a == b:
            return -1
        return na


class Test(unittest.TestCase):
    def test(self):
        self._test('aba', 'cdc', 3)
        self._test('abcd', 'abc', 4)
        self._test('abc', 'dbc', 3)
        self._test('abc', 'abc', -1)

    def _test(self, a, b, expected):
        actual = Solution().findLUSlength(a, b)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
