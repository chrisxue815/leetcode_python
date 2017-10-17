import unittest
import heapq


# O(nlog(h)) time. O(h) space. Binary heap.
class Solution(object):
    def smallestRange(self, nums):
        """
        :type nums: List[List[int]]
        :rtype: List[int]
        """
        q = []
        max_num = -0x80000000
        start = end = length = 0x7FFFFFFF

        for row in nums:
            heapq.heappush(q, (row[0], row, 0))
            max_num = max(max_num, row[0])

        while True:
            min_num, row, index = q[0]

            if max_num - min_num < length:
                length = max_num - min_num
                start = min_num
                end = max_num

            index += 1
            if index == len(row):
                return [start, end]

            max_num = max(max_num, row[index])
            heapq.heapreplace(q, (row[index], row, index))


class Test(unittest.TestCase):
    def test(self):
        self._test([[4, 10, 15, 24, 26], [0, 9, 12, 20], [5, 18, 22, 30]], [20, 24])

    def _test(self, nums, expected):
        actual = Solution().smallestRange(nums)
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()
