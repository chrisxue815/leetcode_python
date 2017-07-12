import unittest


class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        lo = 0
        hi = len(nums) - 1

        while lo <= hi:
            mid = lo + ((hi - lo) >> 1)
            mid_val = nums[mid]
            lo_val = nums[lo]
            hi_val = nums[hi]

            if mid_val == target:
                return True

            if mid_val > lo_val:
                if target < lo_val or target > mid_val:
                    lo = mid + 1
                else:
                    hi = mid - 1
            elif mid_val < lo_val:
                if target < mid_val or target > hi_val:
                    hi = mid - 1
                else:
                    lo = mid + 1
            else:
                if all(num == mid_val for num in nums[lo:mid]):
                    lo = mid + 1
                else:
                    hi = mid - 1

        return False


class Test(unittest.TestCase):
    def test(self):
        self._test([4, 5, 6, 7, 0, 1, 2], 3, False)
        self._test([4, 5, 6, 7, 0, 1, 2], 5, True)
        self._test([4, 5, 6, 4, 0, 1, 4], 5, True)
        self._test([4, 5, 6, 4, 0, 1, 4], 3, False)
        self._test([1, 3, 1, 1, 1], 3, True)
        self._test([1, 1, 1, 3, 1], 3, True)

    def _test(self, nums, target, expected):
        actual = Solution().search(nums, target)
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()
