import unittest


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
        i = lo + (hi - lo) // 2
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

            return (max_of_left + min_of_right) / 2.0


class Solution(object):
    def findMedianSortedArrays(self, a, b):
        k = (len(a) + len(b) - 1) / 2.0
        return _kth(a, b, k)


class Test(unittest.TestCase):
    def test(self):
        self._test([1, 2, 8], [3, 4, 5, 6, 7], 4.5)  # 3 5
        self._test([1, 2, 9], [3, 4, 5, 6, 7, 8], 5)  # 3 6
        self._test([1, 2, 3, 9], [4, 5, 6, 7, 8], 5)  # 4 5
        self._test([1, 2, 3, 10], [4, 5, 6, 7, 8, 9], 5.5)  # 4 6
        self._test([5, 6, 7, 8], [1, 2, 3, 4], 4.5)  # 4 4
        self._test([1, 2, 3, 4], [5, 6, 7, 8, 9], 5)  # 4 5
        self._test([1, 2, 3, 4], [5, 6, 7, 8, 9, 10], 5.5)  # 4 6
        self._test([1, 2, 3], [4, 5, 6, 7, 8, 9], 5)  # 3 7

    def _test(self, nums1, nums2, expected):
        actual = Solution().findMedianSortedArrays(nums1, nums2)
        self.assertEqual(expected, actual)

    def test_kth(self):
        self._test_kth([1, 2, 3], [4, 5, 6], 0, 1)
        self._test_kth([1, 2, 3], [4, 5, 6], 0.5, 1.5)
        self._test_kth([1, 2, 3], [4, 5, 6], 1, 2)
        self._test_kth([1, 2, 3], [4, 5, 6], 5, 6)
        self._test_kth([1], [2, 3, 4, 5, 6], 5, 6)
        self._test_kth([1, 2, 3], [4, 5, 6, 7, 8, 9], 4, 5)

    def _test_kth(self, a, b, k, expected):
        self.assertEqual(expected, _kth(a, b, k))


if __name__ == '__main__':
    unittest.main()
