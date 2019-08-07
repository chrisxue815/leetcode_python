import unittest

import utils


def evaluate_xyz(x, y, z, p, q):
    yz = evaluate_yz(y, z, q)
    return x + yz if p == '+' else x - yz


def evaluate_yz(y, z, q):
    return y * z if q == '*' else y // z


def dfs(s, i):
    # Any expression given by this problem can be reduced to an equivalent general form: x + y * z
    x = 0
    y = 1
    z = 0
    p = '+'
    q = '*'

    while i < len(s):
        c = s[i]

        if ord('0') <= ord(c) <= ord('9'):
            z = z * 10 + ord(c) - ord('0')
        elif c == '+' or c == '-':
            x = evaluate_xyz(x, y, z, p, q)
            y = 1
            z = 0
            p = c
            q = '*'
        elif c == '*' or c == '/':
            y = evaluate_yz(y, z, q)
            z = 0
            q = c
        elif c == '(':
            z, i = dfs(s, i + 1)
        elif c == ')':
            break

        i += 1

    return evaluate_xyz(x, y, z, p, q), i


# O(n) time. O(depth of parentheses) space. One pass, recursion, math reduction.
class Solution:
    def calculate(self, s: str) -> int:
        return dfs(s, 0)[0]


class Test(unittest.TestCase):
    def test(self):
        cases = utils.load_test_json(__file__).test_cases

        for case in cases:
            args = str(case.args)
            actual = Solution().calculate(**case.args.__dict__)
            self.assertEqual(case.expected, actual, msg=args)


if __name__ == '__main__':
    unittest.main()
