import unittest

import utils


# O(n) time. O(depth) space. Stack.
class Solution:
    def scoreOfParentheses(self, S: str) -> int:
        stack = [0]

        for c in S:
            if c == '(':
                stack.append(0)
            else:
                score = stack.pop()
                score = score * 2 if score != 0 else 1
                stack[-1] += score

        return stack[-1]


class Test(unittest.TestCase):
    def test(self):
        cases = utils.load_test_json(__file__).test_cases

        for case in cases:
            args = str(case.args)
            actual = Solution().scoreOfParentheses(**case.args.__dict__)
            self.assertEqual(case.expected, actual, msg=args)


if __name__ == '__main__':
    unittest.main()
