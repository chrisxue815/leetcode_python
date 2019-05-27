import unittest


class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        write_index = 0
        prev = nums[0] - 1

        for num in nums:
            if num != prev:
                nums[write_index] = num
                write_index += 1
                prev = num

        return write_index


class Test(unittest.TestCase):
    def test(self):
        self._test([1, 1, 2], [1, 2])

    def _test(self, nums, expected):
        actual = Solution().removeDuplicates(nums)
        self.assertEqual(len(expected), actual)
        self.assertEqual(expected, nums[:actual])


if __name__ == '__main__':
    unittest.main()
