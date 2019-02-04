import functools
import unittest


class Solution(object):
    def kSmallestPairs(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[List[int]]
        """
        tuples = []
        for i in nums1:
            for j in nums2:
                tuples.append([i, j])

        tuples.sort(key=functools.cmp_to_key(lambda x, y: x[0] + x[1] - y[0] - y[1]))
        return tuples[0:k]


class Test(unittest.TestCase):
    def test(self):
        self._test([1, 7, 11], [2, 4, 6], 3,
                   [[1, 2], [1, 4], [1, 6]])
        self._test([1, 1, 2], [1, 2, 3], 2,
                   [[1, 1], [1, 1]])
        self._test([1, 2], [3], 3,
                   [[1, 3], [2, 3]])

    def _test(self, nums1, nums2, k, expected):
        actual = Solution().kSmallestPairs(nums1, nums2, k)
        self.assertCountEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
