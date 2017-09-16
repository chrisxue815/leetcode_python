import unittest


class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        result = []
        i = 0
        while i < len(nums):
            start = nums[i]
            base_val = start - i
            lo = i + 1
            hi = len(nums) - 1
            while lo <= hi:
                mid = (lo + hi) >> 1
                mid_val = nums[mid]
                expected = base_val + mid
                if mid_val > expected:
                    hi = mid - 1
                else:
                    lo = mid + 1
            if hi == i:
                result.append(str(start))
            else:
                result.append(str(start) + '->' + str(base_val + hi))
            i = lo
        return result


class Test(unittest.TestCase):
    def test(self):
        self._test([0, 1, 2, 4, 5, 7], ['0->2', '4->5', '7'])
        self._test([0, 2, 3, 4, 6, 8, 9], ['0', '2->4', '6', '8->9'])

    def _test(self, nums, expected):
        actual = Solution().summaryRanges(nums)
        self.assertItemsEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()
