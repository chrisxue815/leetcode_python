import unittest


class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums.sort()
        result = []

        for i in xrange(len(nums) - 3):
            a = nums[i]
            if a + nums[i + 1] + nums[i + 2] + nums[i + 3] > target:
                break
            if i > 0 and nums[i - 1] == a or a + nums[-3] + nums[-2] + nums[-1] < target:
                continue
            target_a = target - a

            for j in xrange(i + 1, len(nums) - 2):
                b = nums[j]
                if b + nums[j + 1] + nums[j + 2] > target_a:
                    break
                if j > i + 1 and nums[j - 1] == b or b + nums[-2] + nums[-1] < target_a:
                    continue

                target_b = target_a - b
                lo = j + 1
                hi = len(nums) - 1

                while lo < hi:
                    lo_num = nums[lo]
                    hi_num = nums[hi]
                    sum_ = lo_num + hi_num
                    if sum_ < target_b:
                        lo += 1
                    elif sum_ > target_b:
                        hi -= 1
                    else:
                        result.append([a, b, lo_num, hi_num])
                        lo += 1
                        while lo < hi and nums[lo] == lo_num:
                            lo += 1
                        hi -= 1
                        while lo < hi and nums[hi] == hi_num:
                            hi -= 1
        return result


class Test(unittest.TestCase):
    def test(self):
        self._test(
            [-2, -1, 0, 0, 1, 2],
            0,
            [
                [-1, 0, 0, 1],
                [-2, -1, 1, 2],
                [-2, 0, 0, 2]
            ])

        self._test(
            [0, 0, 0, 0],
            0,
            [
                [0, 0, 0, 0],
            ])

    def _test(self, nums, target, expected):
        actual = Solution().fourSum(nums, target)
        self.assertItemsEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()
