import unittest
from typing import List

import utils


# O(n) time. O(n) space. Stack.
class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack = []
        i = 0

        for x in pushed:
            stack.append(x)

            while stack and stack[-1] == popped[i]:
                stack.pop()
                i += 1

        return len(stack) == 0


class Test(unittest.TestCase):
    def test(self):
        cases = utils.load_test_json(__file__).test_cases

        for case in cases:
            args = str(case.args)
            actual = Solution().validateStackSequences(**case.args.__dict__)
            self.assertEqual(case.expected, actual, msg=args)


if __name__ == '__main__':
    unittest.main()
