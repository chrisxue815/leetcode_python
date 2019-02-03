import unittest


class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        counts = [0] * 256
        for ch in t:
            counts[ord(ch)] += 1
        for ch in s:
            counts[ord(ch)] -= 1
        for i in range(ord('a'), ord('z') + 1):
            if counts[i]:
                return chr(i)


class Test(unittest.TestCase):
    def test(self):
        self._test('abcd', 'abcde', 'e')

    def _test(self, s, t, expected):
        actual = Solution().findTheDifference(s, t)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
