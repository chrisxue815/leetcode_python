import unittest

_a = ord('a')


class Solution:
    def maxProduct(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        if not words:
            return 0

        lengths = {}

        for word in words:
            mask = 0
            for ch in word:
                mask |= 1 << (ord(ch) - _a)
            if len(word) > lengths.get(mask, -1):
                lengths[mask] = len(word)

        return max(len0 * len1 if not mask0 & mask1 else 0
                   for mask1, len1 in list(lengths.items())
                   for mask0, len0 in list(lengths.items()))


class Test(unittest.TestCase):
    def test(self):
        self._test(['abcw', 'baz', 'foo', 'bar', 'xtfn', 'abcdef'], 16)
        self._test(['a', 'ab', 'abc', 'd', 'cd', 'bcd', 'abcd'], 4)
        self._test(['a', 'aa', 'aaa', 'aaaa'], 0)

    def _test(self, words, expected):
        actual = Solution().maxProduct(words)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
