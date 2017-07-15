import unittest


class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        num_to_index = {}
        half = target >> 1

        for i, num in enumerate(nums):
            if num in num_to_index and num == half:
                return [num_to_index[num], i]
            num_to_index[num] = i

        nums.sort()

        for i, num in enumerate(nums):
            diff = target - num
            lo = i + 1
            hi = len(nums) - 1

            while lo <= hi:
                mid = lo + ((hi - lo) >> 1)
                mid_num = nums[mid]

                if mid_num < diff:
                    lo = mid + 1
                elif mid_num > diff:
                    hi = mid - 1
                else:
                    return [num_to_index[num], num_to_index[mid_num]]


class Test(unittest.TestCase):
    def test(self):
        self._test([2, 7, 11, 15], 9, [0, 1])
        self._test([11, 2, 7, 15], 9, [1, 2])
        self._test([2, 7, 11, 7, 15], 14, [1, 3])

    def _test(self, nums, target, expected):
        actual = Solution().twoSum(nums, target)
        self.assertItemsEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()
