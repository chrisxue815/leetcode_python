import unittest


class Solution(object):
    def maximumProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max1, max2, max3, min1, min2 = -1000, -1000, -1000, 1000, 1000
        for num in nums:
            if num > max3:
                if num >= max2:
                    if num >= max1:
                        max1, max2, max3 = num, max1, max2
                    else:
                        max2, max3 = num, max2
                else:
                    max3 = num
            if num < min2:
                if num <= min1:
                    min1, min2 = num, min1
                else:
                    min2 = num
        return max(max1 * max2 * max3, max1 * min1 * min2)


class Test(unittest.TestCase):
    def test(self):
        self._test([1, 2, 3], 6)
        self._test([1, 2, 3, 4], 24)
        self._test([1, 2, 3, -4, -5], 60)
        self._test([1, 2, 3, -4], 6)
        self._test([1, 2, -3, -4], 24)
        self._test([1, 2, -3, 0], 0)
        self._test([1, 2, -3], -6)
        self._test([1, -2, -3, -4], 12)
        self._test([1, -2, 0], 0)
        self._test([1, 0, 0], 0)
        self._test([-1, -2, -3, 0], 0)
        self._test([-1, -2, -3, -4], -6)

    def _test(self, nums, expected):
        actual = Solution().maximumProduct(nums)
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()
