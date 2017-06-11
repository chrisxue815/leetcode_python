import unittest


class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        n = ord('z') + 1
        counts = [0] * n
        for ch in s:
            counts[ord(ch)] += 1
        chars = []
        for ch in xrange(n):
            if counts[ch]:
                chars.append((counts[ch], chr(ch)))
        chars.sort(reverse=True)
        ret = []
        for occur, ch in chars:
            ret += [ch] * occur
        return ''.join(ret)


class Test(unittest.TestCase):
    def test(self):
        self._test('tree', 'eetr')
        self._test('cccaaa', 'cccaaa')
        self._test('Aabb', 'bbaA')

    def _test(self, s, expected):
        actual = Solution().frequencySort(s)
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()
