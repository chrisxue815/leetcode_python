import unittest

import utils

DIFF = ord('a') - ord('A')


# O(n) time. O(n) space. Iteration, stack.
class Solution:
    def makeGood(self, s: str) -> str:
        stack = []

        for c in s:
            if stack and abs(ord(stack[-1]) - ord(c)) == DIFF:
                stack.pop()
            else:
                stack.append(c)

        return ''.join(stack)


class Test(unittest.TestCase):
    def test(self):
        cases = utils.load_test_json(__file__).test_cases

        for case in cases:
            args = str(case.args)
            actual = Solution().makeGood(**case.args.__dict__)
            self.assertEqual(case.expected, actual, msg=args)


if __name__ == '__main__':
    unittest.main()
