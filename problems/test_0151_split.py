import unittest


class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        return ' '.join(reversed(s.split()))


class Test(unittest.TestCase):
    def test(self):
        self._test("  the sky is    blue   ", "blue is sky the")
        self._test("     ", "")

    def _test(self, s, expected):
        actual = Solution().reverseWords(s)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
