import unittest


class Solution:
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        if not nums1:
            return []

        set1 = set(nums1)
        set1.intersection_update(nums2)
        return list(set1)


class Test(unittest.TestCase):
    def test(self):
        self._test([1, 2, 2, 1], [2, 2], [2])
        self._test([], [1], [])
        self._test([2, 1], [1, 2], [1, 2])

    def _test(self, nums1, nums2, result):
        actual = Solution().intersection(nums1, nums2)
        self.assertEqual(result, actual)


if __name__ == '__main__':
    unittest.main()
