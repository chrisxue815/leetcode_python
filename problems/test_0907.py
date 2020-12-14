import unittest
from typing import List

import utils

BOUND = 10 ** 9 + 7


# O(n) time. O(n) space. Monotone stack.
class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        result = 0
        arr.append(0)
        stack = []

        for i, x in enumerate(arr):
            while stack and arr[stack[-1]] > x:
                j = stack.pop()
                k = stack[-1] if stack else -1
                result += arr[j] * (i - j) * (j - k)
                result %= BOUND
            stack.append(i)

        return result


class Test(unittest.TestCase):
    def test(self):
        cases = utils.load_test_json(__file__).test_cases

        for case in cases:
            args = str(case.args)
            actual = Solution().sumSubarrayMins(**case.args.__dict__)
            self.assertEqual(case.expected, actual, msg=args)


if __name__ == '__main__':
    unittest.main()
