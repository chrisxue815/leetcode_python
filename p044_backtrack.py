import unittest


class Solution(object):
    def isMatch(self, s, p):
        si = 0
        pi = 0
        pi_star = -1
        si_star = -1

        while si < len(s):
            p_char = p[pi] if pi < len(p) else 0

            if p_char == '?' or p_char == s[si]:
                pi += 1
                si += 1
            elif p_char == '*':
                pi += 1
                pi_star = pi
                si_star = si
            elif pi_star != -1:
                pi = pi_star
                si_star += 1
                si = si_star
            else:
                return False

        while pi < len(p):
            if p[pi] != '*':
                return False
            pi += 1

        return True


class Test(unittest.TestCase):
    def test(self):
        self._test('aa', 'a', False)
        self._test('aa', 'aa', True)
        self._test('aaa', 'aa', False)
        self._test('aa', '*', True)
        self._test('aa', 'a*', True)
        self._test('ab', '?*', True)
        self._test('aab', 'c*a*b', False)

        # * matches 0 occurrence
        self._test('aa', '*aa', True)
        self._test('aa', 'aa*', True)
        self._test('', '*', True)
        self._test('', '?', False)

        self._test('', '', True)
        self._test('a', '', False)

    def _test(self, s, p, expected):
        actual = Solution().isMatch(s, p)
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()
