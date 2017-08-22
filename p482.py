import unittest


class Solution(object):
    def licenseKeyFormatting(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        alphanum_len = len(s) - s.count('-')
        result = [''] * (alphanum_len + (alphanum_len - 1) // k)
        group_len = alphanum_len % k or k
        r = 0

        for w in xrange(len(result)):
            while s[r] == '-':
                r += 1
            if group_len:
                result[w] = s[r].upper()
                r += 1
                group_len -= 1
            else:
                result[w] = '-'
                group_len = k

        return ''.join(result)


class Test(unittest.TestCase):
    def test(self):
        self._test('2-4A0r7-4k', 4, '24A0-R74K')
        self._test('2-4A0r7-4k', 3, '24-A0R-74K')

    def _test(self, s, k, expected):
        actual = Solution().licenseKeyFormatting(s, k)
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()
