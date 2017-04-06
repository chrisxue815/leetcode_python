import unittest


class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        duplicates = []

        for num in nums:
            index = abs(num) - 1
            next_num = nums[index]
            if next_num < 0:
                duplicates.append(index + 1)
            else:
                nums[index] = -next_num

        return duplicates


class Test(unittest.TestCase):
    def test(self):
        self._test([4, 3, 2, 7, 8, 2, 3, 1], [2, 3])
        self._test([2, 1], [])
        self._test([3, 3, 1], [3])
        self._test([1], [])
        self._test([1, 1], [1])
        self._test([2, 1, 1], [1])

    def _test(self, nums, expected):
        actual = Solution().findDuplicates(nums)
        self.assertItemsEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()
