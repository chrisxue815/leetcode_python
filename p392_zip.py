import unittest


class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if not s:
            return True

        s_index = 0
        s_val = s[s_index]
        for t_val in t:
            if t_val == s_val:
                s_index += 1
                if s_index == len(s):
                    return True
                s_val = s[s_index]
        return False


class Test(unittest.TestCase):
    def test(self):
        self._test('ace', 'abcde', True)
        self._test('aec', 'abcde', False)

    def _test(self, s, t, expected):
        actual = Solution().isSubsequence(s, t)
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()
