import unittest


class Solution:
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        lo = 1
        hi = len(nums) - 1

        while lo <= hi:
            mid = lo + ((hi - lo) >> 1)
            count_smaller = 0
            count_mid = 0
            for i in nums:
                if i < mid:
                    count_smaller += 1
                elif i == mid:
                    count_mid += 1
                    if count_mid > 1:
                        return mid

            if count_smaller >= mid:
                hi = mid - 1
            else:
                lo = mid + 1

        raise RuntimeError


class Test(unittest.TestCase):
    def test(self):
        self._test([1, 2, 3, 4, 4, 5], 4)
        self._test([4, 5, 3, 4, 1, 2], 4)
        self._test([1, 2, 3, 4, 5, 5, 6], 5)
        self._test([1, 3, 4, 5, 6, 6, 6], 6)
        self._test([1, 3, 4, 5, 6, 6, 6, 7], 6)
        self._test([1, 3, 4, 2, 1], 1)

    def _test(self, nums, expected):
        actual = Solution().findDuplicate(nums)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
