import unittest


class Solution(object):
    def isMatch(self, s, p):
        return self._dfs(s, p, 0, 0)

    def _dfs(self, s, p, si, pi):
        while True:
            if pi == len(p):
                if si == len(s):
                    return True
                else:
                    return False

            curr_pattern = p[pi]

            if curr_pattern == '*':
                next_pi = pi + 1
                while next_pi < len(p) and p[next_pi] == '*':
                    next_pi += 1
                next_si = si
                while next_si <= len(s):
                    if self._dfs(s, p, next_si, next_pi):
                        return True
                    # Optimize: advance to the next * if all characters in-between have matched
                    next_si += 1
                return False

            else:
                if si == len(s):
                    return False

                if curr_pattern == '?':
                    si += 1
                    pi += 1

                else:
                    curr_char = s[si]
                    if curr_char != curr_pattern:
                        return False
                    si += 1
                    pi += 1


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

    def _test(self, s, p, expected):
        actual = Solution().isMatch(s, p)
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()
