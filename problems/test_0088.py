import unittest


class Solution:
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        hi = m + n - 1
        m -= 1
        n -= 1
        while m >= 0 and n >= 0:
            if nums1[m] > nums2[n]:
                nums1[hi] = nums1[m]
                m -= 1
            else:
                nums1[hi] = nums2[n]
                n -= 1
            hi -= 1
        if n >= 0:
            nums1[:n + 1] = nums2[:n + 1]


class Test(unittest.TestCase):
    def test(self):
        self._test(
            [10, 20],
            [1, 2, 11, 12, 21, 22],
            [1, 2, 10, 11, 12, 20, 21, 22])

    def _test(self, nums1, nums2, expected):
        m = len(nums1)
        n = len(nums2)
        nums1 += [0] * n
        actual = Solution().merge(nums1, m, nums2, n)
        self.assertEqual(expected, nums1)


if __name__ == '__main__':
    unittest.main()
