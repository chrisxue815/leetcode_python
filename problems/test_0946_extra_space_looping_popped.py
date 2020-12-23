import unittest
from typing import List

import utils


# O(n) time. O(n) space. Stack.
class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack = []
        i = 0

        for x in popped:
            if stack and stack[-1] == x:
                stack.pop()
            else:
                while i < len(pushed):
                    if pushed[i] == x:
                        i += 1
                        break
                    stack.append(pushed[i])
                    i += 1
                else:
                    return False

        return True


class Test(unittest.TestCase):
    def test(self):
        cases = utils.load_test_json(__file__).test_cases

        for case in cases:
            args = str(case.args)
            actual = Solution().validateStackSequences(**case.args.__dict__)
            self.assertEqual(case.expected, actual, msg=args)


if __name__ == '__main__':
    unittest.main()
