import unittest


class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ''

        result = []
        min_len = min(len(s) for s in strs)

        for i in range(min_len):
            ch = strs[0][i]
            if all(s[i] == ch for s in strs):
                result.append(ch)
            else:
                break

        return ''.join(result)


class Test(unittest.TestCase):
    def test(self):
        self._test([
            'abcd_e',
            'abcd_fg',
            'abcd_fh',
        ], 'abcd_')

    def _test(self, strs, expected):
        actual = Solution().longestCommonPrefix(strs)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
