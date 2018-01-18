import unittest


class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        if len(s) <= k:
            return len(s)

        counts = [0] * 128
        lo = max_count = 0

        for hi, hi_ch in enumerate(s):
            counts[ord(hi_ch)] += 1
            max_count = max(max_count, counts[ord(hi_ch)])

            if hi - lo + 1 - max_count > k:
                counts[ord(s[lo])] -= 1
                lo += 1

        return len(s) - lo


class Test(unittest.TestCase):
    def test(self):
        self._test('ABAB', 2, 4)
        self._test('AABABBA', 1, 4)
        self._test('AAAA', 5, 4)
        self._test('AAAA', 2, 4)

    def _test(self, s, k, expected):
        actual = Solution().characterReplacement(s, k)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
