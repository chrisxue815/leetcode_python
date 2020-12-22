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
class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        si = len(S) - 1
        ti = len(T) - 1

        while True:
            si = backspace(S, si)
            ti = backspace(T, ti)

            if si < 0:
                return ti < 0
            if ti < 0:
                return False
            if S[si] != T[ti]:
                return False
            si -= 1
            ti -= 1


class Test(unittest.TestCase):
    def test(self):
        cases = utils.load_test_json(__file__).test_cases

        for case in cases:
            args = str(case.args)
            actual = Solution().backspaceCompare(**case.args.__dict__)
            self.assertEqual(case.expected, actual, msg=args)


if __name__ == '__main__':
    unittest.main()
