import unittest


# O(n). Two pointers.
class Solution(object):
    def numSubarrayProductLessThanK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if k <= 0:
            return 0

        result = 0
        n = len(nums)
        product = 1  # [lo, hi)
        hi = 0

        for lo, lo_num in enumerate(nums):
            while hi < n:
                new_product = product * nums[hi]
                if new_product >= k:
                    break
                product = new_product
                hi += 1

            result += hi - lo
            if lo < hi:
                product /= lo_num
            else:
                hi += 1

        return result


class Test(unittest.TestCase):
    def test(self):
        self._test([10, 5, 2, 6], 100, 8)
        self._test([10, 5, 2, 6], 0, 0)
        self._test([3, 3, 3], 2, 0)
        self._test([1, 1, 1], 1, 0)

    def _test(self, n, k, expected):
        actual = Solution().numSubarrayProductLessThanK(n, k)
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()
