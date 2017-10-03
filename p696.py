import unittest


# O(n)
class Solution(object):
    def countBinarySubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        count = 0
        prev_start = 0
        curr_start = 0
        curr = s[0]
        for i in xrange(1, len(s)):
            if s[i] != curr:
                count += min(curr_start - prev_start, i - curr_start)
                prev_start, curr_start = curr_start, i
                curr = s[i]
        return count + min(curr_start - prev_start, len(s) - curr_start)


class Test(unittest.TestCase):
    def test(self):
        self._test('00110011', 6)
        self._test('10101', 4)
        self._test('1001', 2)

    def _test(self, s, expected):
        actual = Solution().countBinarySubstrings(s)
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()
