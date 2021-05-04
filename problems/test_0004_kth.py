import unittest
from typing import List

import utils


def _kth(a, b, k):
    m = len(a)
    n = len(b)
    if m > n:
        a, b, m, n = b, a, n, m

    kfloor = int(k)
    kceil = kfloor + 1
    lo = max(0, kceil - n)
    hi = min(m, kceil)

    while True:
        i = lo + ((hi - lo) >> 1)
        j = kceil - i

        if i > 0 and j < n and a[i - 1] > b[j]:
            hi = i - 1
        elif j > 0 and i < m and b[j - 1] > a[i]:
            lo = i + 1
        else:
            if i == 0:
                max_of_left = b[j - 1]
            elif j == 0:
                max_of_left = a[i - 1]
            else:
                max_of_left = max(a[i - 1], b[j - 1])

            if kfloor == k:
                return max_of_left

            if i == m:
                min_of_right = b[j]
            elif j == n:
                min_of_right = a[i]
            else:
                min_of_right = min(a[i], b[j])

            return (max_of_left + min_of_right) / 2


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        k = (len(nums1) + len(nums2) - 1) / 2
        return _kth(nums1, nums2, k)


class Test(unittest.TestCase):
    def test(self):
        utils.test(self, __file__, Solution)


if __name__ == '__main__':
    unittest.main()
