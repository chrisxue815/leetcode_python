import unittest


# O(n)
class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if not nums:
            return False
        lo = new_lo = nums[0]
        mid = 0x7fffffff
        for num in nums:
            if lo == new_lo:
                if num <= lo:
                    new_lo = num
                elif num < mid:
                    mid = num
                elif num > mid:
                    return True
            else:
                if num <= new_lo:
                    new_lo = num
                elif num <= mid:
                    lo = new_lo
                    mid = num
                else:
                    return True

        return False


class Test(unittest.TestCase):
    def test(self):
        self._test([1, 2, 3, 4, 5], True)
        self._test([5, 4, 3, 2, 1], False)

    def _test(self, n, expected):
        actual = Solution().increasingTriplet(n)
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()
