import unittest
from typing import List

import utils


# O(n) time. O(n) space. Monotone stack.
class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        result = [0] * len(T)
        stack = []

        for i, t in enumerate(T):
            while stack and stack[-1][1] < t:
                j, _ = stack.pop()
                result[j] = i - j
            stack.append((i, t))

        return result


class Test(unittest.TestCase):
    def test(self):
        cases = utils.load_test_json(__file__).test_cases

        for case in cases:
            args = str(case.args)
            actual = Solution().dailyTemperatures(**case.args.__dict__)
            self.assertEqual(case.expected, actual, msg=args)


if __name__ == '__main__':
    unittest.main()
