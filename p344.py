import unittest


class Solution(object):
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        # return s[::-1]
        s = list(s)
        lo = 0
        hi = len(s) - 1
        while lo < hi:
            s[lo], s[hi] = s[hi], s[lo]
            lo += 1
            hi -= 1
        return ''.join(s)


class Test(unittest.TestCase):
    def test(self):
        self._test('hello', 'olleh')

    def _test(self, s, expected):
        actual = Solution().reverseString(s)
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()
