import unittest


class Solution(object):
    def findClosestElements(self, arr, k, x):
        """
        :type arr: List[int]
        :type k: int
        :type x: int
        :rtype: List[int]
        """
        lo = 0
        hi = len(arr) - 1

        while lo <= hi:
            mid = lo + ((hi - lo) >> 1)
            mid_val = arr[mid]
            if mid_val < x:
                lo = mid + 1
            elif mid_val > x:
                hi = mid - 1
            else:
                lo = hi = mid

                break

        lo, hi = hi, lo

        while hi - lo - 1 < k:
            if hi == len(arr) or lo >= 0 and x - arr[lo] <= arr[hi] - x:
                lo -= 1
            else:
                hi += 1

        return arr[lo + 1:hi]


class Test(unittest.TestCase):
    def test(self):
        self._test([1, 2, 3, 4, 5], 4, 3, [1, 2, 3, 4])
        self._test([1, 2, 3, 4, 5], 4, -1, [1, 2, 3, 4])
        self._test([1, 2, 3, 4, 5], 4, 6, [2, 3, 4, 5])
        self._test([0, 0, 1, 2, 3, 3, 4, 7, 7, 8], 3, 5, [3, 3, 4])

    def _test(self, arr, k, x, expected):
        actual = Solution().findClosestElements(arr, k, x)
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()
