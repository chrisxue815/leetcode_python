import unittest
import utils


def backspace(s, si):
    num_backspace = 0
    while si >= 0:
        if s[si] == '#':
            num_backspace += 1
        elif num_backspace == 0:
            break
        else:
            num_backspace -= 1
        si -= 1
    return si


# O(n) time. O(1) space. Iteration.
class Solution(object):
    def backspaceCompare(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        si = len(s) - 1
        ti = len(t) - 1

        while True:
            si = backspace(s, si)
            ti = backspace(t, ti)

            if si < 0:
                return ti < 0
            if ti < 0:
                return False
            if s[si] != t[ti]:
                return False
            si -= 1
            ti -= 1


class Test(unittest.TestCase):
    def test(self):
        cases = utils.load_test_json(__file__).test_cases

        for case in cases:
            actual = Solution().backspaceCompare(**case.args._asdict())
            self.assertEqual(case.expected, actual)


if __name__ == '__main__':
    unittest.main()
