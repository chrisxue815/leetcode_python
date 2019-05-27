import unittest


class Solution:
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        lo = 0
        hi = len(nums) - 1

        while lo <= hi:
            mid = lo + ((hi - lo) >> 1)
            mid_val = nums[mid]

            if mid_val < target:
                lo = mid + 1
            elif mid_val > target:
                hi = mid - 1
            else:
                mid_tmp = mid
                hi_tmp = hi
                hi = mid
                while lo <= hi:
                    mid = lo + ((hi - lo) >> 1)
                    if nums[mid] < target:
                        lo = mid + 1
                    else:
                        hi = mid - 1
                start = lo

                lo = mid_tmp
                hi = hi_tmp
                while lo <= hi:
                    mid = lo + ((hi - lo) >> 1)
                    if nums[mid] > target:
                        hi = mid - 1
                    else:
                        lo = mid + 1

                return [start, hi]

        return [-1, -1]


class Test(unittest.TestCase):
    def test(self):
        self._test([5, 7, 7, 8, 8, 10], 8, [3, 4])

    def _test(self, nums, target, expected):
        actual = Solution().searchRange(nums, target)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
