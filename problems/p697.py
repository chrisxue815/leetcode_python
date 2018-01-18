import unittest
import collections


# O(n) time. O(n) space. Hash table.
class Solution(object):
    def findShortestSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ranges = {}

        for i, num in enumerate(nums):
            r = ranges.get(num)
            if r is None:
                r = [i, i]
                ranges[num] = r
            else:
                r[1] = i

        min_range = 0x7FFFFFFF
        counts = collections.Counter(nums)
        degree = counts.most_common(1)[0][1]

        for num, count in counts.iteritems():
            if count == degree:
                r = ranges[num]
                min_range = min(min_range, r[1] - r[0])

        return min_range + 1


class Test(unittest.TestCase):
    def test(self):
        self._test([1, 2, 2, 3, 1], 2)
        self._test([1, 2, 2, 3, 1, 4, 2], 6)
        self._test([2, 2, 1, 4, 1, 3, 3], 2)

    def _test(self, nums, expected):
        actual = Solution().findShortestSubArray(nums)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
