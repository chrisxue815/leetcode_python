import unittest
from collections import defaultdict


class Solution:
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        if not nums1:
            return []

        count1 = defaultdict(lambda: 0)
        for num in nums1:
            count1[num] += 1

        result = []
        for num in nums2:
            if count1.get(num, 0) > 0:
                count1[num] -= 1
                result.append(num)

        return result


class Test(unittest.TestCase):
    def test(self):
        self._test([1, 2, 2, 1], [2, 2], [2, 2])
        self._test([], [1], [])
        self._test([2, 1], [1, 2], [1, 2])

    def _test(self, nums1, nums2, result):
        actual = Solution().intersect(nums1, nums2)
        self.assertEqual(result, actual)


if __name__ == '__main__':
    unittest.main()
