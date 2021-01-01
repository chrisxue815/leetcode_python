import unittest

import utils


# O(n) time. O(1) space. Space-optimized stack.
class Solution:
    def scoreOfParentheses(self, S: str) -> int:
        result = 0
        depth = -1

        for i, c in enumerate(S):
            if c == '(':
                depth += 1
            else:
                if S[i - 1] == '(':
                    result += 1 << depth
                depth -= 1

        return result


class Test(unittest.TestCase):
    def test(self):
        cases = utils.load_test_json(__file__).test_cases

        for case in cases:
            args = str(case.args)
            actual = Solution().scoreOfParentheses(**case.args.__dict__)
            self.assertEqual(case.expected, actual, msg=args)


if __name__ == '__main__':
    unittest.main()
