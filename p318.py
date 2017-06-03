import unittest

_a = ord('a')


class Solution(object):
    def maxProduct(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        n = len(words)
        mask_and_len = [None] * n

        for i in xrange(n):
            mask = 0
            word = words[i]
            for ch in word:
                mask |= 1 << (ord(ch) - _a)
            mask_and_len[i] = (mask, len(word))

        max_product = 0
        for i in xrange(n):
            for j in xrange(i + 1, n):
                if mask_and_len[i][0] & mask_and_len[j][0] == 0:
                    product = mask_and_len[i][1] * mask_and_len[j][1]
                    if product > max_product:
                        max_product = product
        return max_product


class Test(unittest.TestCase):
    def test(self):
        self._test(['abcw', 'baz', 'foo', 'bar', 'xtfn', 'abcdef'], 16)
        self._test(['a', 'ab', 'abc', 'd', 'cd', 'bcd', 'abcd'], 4)
        self._test(['a', 'aa', 'aaa', 'aaaa'], 0)

    def _test(self, words, expected):
        actual = Solution().maxProduct(words)
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()
