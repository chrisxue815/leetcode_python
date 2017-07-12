import unittest


class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        lo = 0
        hi = len(nums) - 1

        while lo <= hi:
            mid = lo + ((hi - lo) >> 1)
            mid_val = nums[mid]

            if target == mid_val:
                return mid

            lo_val = nums[lo]
            hi_val = nums[hi]

            if mid_val >= lo_val:
                if target > mid_val or target < lo_val:
                    lo = mid + 1
                else:
                    hi = mid - 1
            elif mid_val < lo_val:
                if target < mid_val or target > hi_val:
                    hi = mid - 1
                else:
                    lo = mid + 1

        return -1


class Test(unittest.TestCase):
    def test(self):
        self._test([4, 5, 6, 7, 0, 1, 2], 3, -1)
        self._test([4, 5, 6, 7, 0, 1, 2], 5, 1)
        self._test([1, 3], 2, -1)

    def _test(self, nums, target, expected):
        actual = Solution().search(nums, target)
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()
