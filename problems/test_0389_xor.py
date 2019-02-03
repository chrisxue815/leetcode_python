import unittest


class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        result = 0
        for ch in s:
            result ^= ord(ch)
        for ch in t:
            result ^= ord(ch)
        return chr(result)


class Test(unittest.TestCase):
    def test(self):
        self._test('abcd', 'abcde', 'e')

    def _test(self, s, t, expected):
        actual = Solution().findTheDifference(s, t)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
