import unittest
from typing import List

import utils


# O(n) time. O(n) space. Monotone stack.
class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        result = [-1] * len(nums)
        stack = []

        for i, num in enumerate(nums):
            while stack and nums[stack[-1]] < num:
                result[stack.pop()] = num

            stack.append(i)

        i = 1
        while i < len(stack) and nums[stack[i]] == nums[stack[0]]:
            i += 1
        if i >= len(stack):
            return result
        stack = stack[i:]

        for num in nums:
            while nums[stack[-1]] < num:
                result[stack.pop()] = num
                if not stack:
                    return result


class Test(unittest.TestCase):
    def test(self):
        cases = utils.load_test_json(__file__).test_cases

        for case in cases:
            args = str(case.args)
            actual = Solution().nextGreaterElements(**case.args.__dict__)
            self.assertEqual(case.expected, actual, msg=args)


if __name__ == '__main__':
    unittest.main()
