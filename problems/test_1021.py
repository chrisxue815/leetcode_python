import unittest

import utils


# O(n) time. O(1) space. Space-optimized stack.
class Solution:
    def removeOuterParentheses(self, S: str) -> str:
        result = ''
        lo = 1
        count = 0

        for hi, ch in enumerate(S):
            count += 1 if ch == '(' else -1
            if count == 0:
                result += S[lo:hi]
                lo = hi + 2

        return result


class Test(unittest.TestCase):
    def test(self):
        cases = utils.load_test_json(__file__).test_cases

        for case in cases:
            args = str(case.args)
            actual = Solution().removeOuterParentheses(**case.args.__dict__)
            self.assertEqual(case.expected, actual, msg=args)


if __name__ == '__main__':
    unittest.main()
