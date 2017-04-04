import unittest


class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if not nums:
            return

        n = len(nums)

        # for every i < left, nums[i] == 0
        left = 0
        while left < n and nums[left] == 0:
            left += 1

        # for every i > right, nums[i] == 2
        right = n - 1
        while right >= 0 and nums[right] == 2:
            right -= 1

        # for every left <= i < mid, nums[i] == 1
        mid = left
        while mid <= right:
            if nums[mid] == 0:
                nums[mid], nums[left] = nums[left], nums[mid]
                left += 1
            elif nums[mid] == 2:
                if nums[right] == 1:
                    nums[mid], nums[right] = nums[right], nums[mid]
                else:
                    nums[mid], nums[right] = nums[right], nums[mid]
                    nums[mid], nums[left] = nums[left], nums[mid]
                    left += 1
                while True:
                    right -= 1
                    if right == mid or nums[right] != 2:
                        break
            mid += 1


class Test(unittest.TestCase):
    def test(self):
        self._test([], [])
        self._test([0], [0])
        self._test([2, 0, 1], [0, 1, 2])
        self._test([2, 0], [0, 2])
        self._test([1, 2, 0, 0], [0, 0, 1, 2])
        self._test([1, 2, 0], [0, 1, 2])
        self._test([2, 1, 0, 1], [0, 1, 1, 2])

    def _test(self, nums, expected):
        Solution().sortColors(nums)
        self.assertEqual(nums, expected)


if __name__ == '__main__':
    unittest.main()
