import unittest
import itertools


class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n <= 2:
            return n
        write_index = 2

        for num in itertools.islice(nums, 2, n):
            if num != nums[write_index - 2]:
                nums[write_index] = num
                write_index += 1

        return write_index


class Test(unittest.TestCase):
    def test(self):
        self._test([1, 1, 1, 2, 2, 3], [1, 1, 2, 2, 3])

    def _test(self, nums, expected):
        actual = Solution().removeDuplicates(nums)
        self.assertEqual(len(expected), actual)
        self.assertEqual(expected, nums[:actual])


if __name__ == '__main__':
    unittest.main()
