import unittest


class Solution:
    def nextGreaterElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        result = [-1] * len(nums)
        stack = []

        for i in range(len(nums)):
            num = nums[i]
            while stack and num > nums[stack[-1]]:
                result[stack.pop()] = num
            stack.append(i)

        i = 1
        while i < len(stack) and stack[i] == stack[0]:
            i += 1
        stack = stack[i:]

        for num in nums:
            while stack:
                if num <= nums[stack[-1]]:
                    break
                result[stack.pop()] = num
            else:
                break

        return result


class Test(unittest.TestCase):
    def test(self):
        self._test([1, 2, 1], [2, -1, 2])

    def _test(self, nums, expected):
        actual = Solution().nextGreaterElements(nums)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
