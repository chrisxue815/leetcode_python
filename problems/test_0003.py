import unittest


class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        counts = [0] * 128
        max_len = 0
        lo = 0

        for hi in range(len(s)):
            hi_ch = ord(s[hi])
            counts[hi_ch] += 1

            if counts[hi_ch] > 1:
                new_len = hi - lo
                if new_len > max_len:
                    max_len = new_len

                while True:
                    lo_ch = ord(s[lo])
                    lo += 1
                    counts[lo_ch] -= 1
                    if lo_ch == hi_ch:
                        break

        return max(max_len, len(s) - lo)


class Test(unittest.TestCase):
    def test(self):
        self._test('abcabcbb', 3)
        self._test('bbbbb', 1)
        self._test('pwwkew', 3)
        self._test('abc', 3)
        self._test('abcad', 4)

    def _test(self, s, expected):
        actual = Solution().lengthOfLongestSubstring(s)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
