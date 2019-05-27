import unittest


class Solution:
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        write_index = 0
        for read_index in range(len(nums)):
            if nums[read_index]:
                nums[write_index] = nums[read_index]
                write_index += 1

        for write_index in range(write_index, len(nums)):
            nums[write_index] = 0

        return nums


class Test(unittest.TestCase):
    def test(self):
        self._test([0, 1, 0, 3, 12], [1, 3, 12, 0, 0])

    def _test(self, nums, expected):
        Solution().moveZeroes(nums)
        self.assertEqual(expected, nums)


if __name__ == '__main__':
    unittest.main()
