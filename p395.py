import unittest


class Solution(object):
    def longestSubstring(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        if len(s) < k:
            return 0
        counts = [0] * 26
        for ch in s:
            counts[ord(ch) - ord('a')] += 1
        for ch, count in enumerate(counts):
            if 0 < count < k:
                return max(self.longestSubstring(seg, k) for seg in s.split(chr(ch + ord('a'))))
        return len(s)


class Test(unittest.TestCase):
    def test(self):
        self._test('aaabb', 3, 3)
        self._test('ababbc', 2, 5)

    def _test(self, s, k, expected):
        actual = Solution().longestSubstring(s, k)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
