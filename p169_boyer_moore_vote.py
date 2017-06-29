import unittest
import itertools


class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        leading = nums[0]
        count = 0

        for num in itertools.islice(nums, 1, len(nums)):
            if num == leading:
                count += 1
            elif count > 0:
                count -= 1
            else:
                leading = num
        return leading


class Test(unittest.TestCase):
    def test(self):
        self._test([1, 2, 2, 2], 2)
        self._test([1, 2, 2, 2, 1], 2)
        self._test([-1], -1)

    def _test(self, nums, expected):
        actual = Solution().majorityElement(nums)
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()
