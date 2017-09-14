import unittest


class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        result = []
        for ia, a in enumerate(nums):
            if ia > 0 and nums[ia - 1] == a:
                continue
            residual = -a
            lo = ia + 1
            hi = len(nums) - 1
            while lo < hi:
                lo_num = nums[lo]
                hi_num = nums[hi]
                s = lo_num + hi_num
                if s < residual:
                    lo += 1
                    while lo < hi and nums[lo] == lo_num:
                        lo += 1
                elif s > residual:
                    hi -= 1
                    while lo < hi and nums[hi] == hi_num:
                        hi -= 1
                else:
                    result.append([a, lo_num, hi_num])
                    lo += 1
                    hi -= 1
                    while lo < hi and nums[lo] == lo_num:
                        lo += 1
                    while lo < hi and nums[hi] == hi_num:
                        hi -= 1

        return result


class Test(unittest.TestCase):
    def test(self):
        self._test([-1, 0, 1, 2, -1, -4], [
            [-1, 0, 1],
            [-1, -1, 2],
        ])
        self._test([-1, -1, 0, 1], [
            [-1, 0, 1],
        ])

    def _test(self, nums, expected):
        actual = Solution().threeSum(nums)
        self.assertItemsEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()
