import unittest
import collections


class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        c = collections.Counter(t)
        c.subtract(s)
        return c.most_common(1)[0][0]


class Test(unittest.TestCase):
    def test(self):
        self._test('abcd', 'abcde', 'e')

    def _test(self, s, t, expected):
        actual = Solution().findTheDifference(s, t)
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()
