import unittest


class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        n = len(s)
        s = list(s)
        lo = 0
        for hi in xrange(n):
            if s[hi] == ' ':
                s[lo:hi] = reversed(s[lo:hi])
                lo = hi + 1
        if lo < n:
            s[lo:n] = reversed(s[lo:n])

        return ''.join(s)


class Test(unittest.TestCase):
    def test(self):
        self._test("Let's take LeetCode contest", "s'teL ekat edoCteeL tsetnoc")

    def _test(self, s, expected):
        actual = Solution().reverseWords(s)
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()
