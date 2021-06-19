import unittest

import utils


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
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
        utils.test(self, __file__, Solution)


if __name__ == '__main__':
    unittest.main()
