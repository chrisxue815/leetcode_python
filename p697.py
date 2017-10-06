import unittest
import collections


# O(nlog(n))
class Solution(object):
    def findShortestSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0

        counter = collections.Counter(nums)
        most_common = counter.most_common()
        degree = most_common[0][1]

        pending = set()
        for num, count in most_common:
            if count != degree:
                break
            pending.add(num)

        lo = 0
        hi = len(nums) - 1
        while True:
            while nums[lo] not in pending:
                lo += 1
            while nums[hi] not in pending:
                hi -= 1
            if len(pending) == 1:
                return hi - lo + 1
            elif nums[lo] == nums[hi]:
                pending.remove(nums[lo])
            elif len(pending) >= 3:
                pending.remove(nums[lo])
                pending.remove(nums[hi])
            else:
                mid = hi
                while nums[mid] != nums[lo]:
                    mid -= 1
                lo_len = mid - lo
                mid = lo
                while nums[mid] != nums[hi]:
                    mid += 1
                hi_len = hi - mid
                return min(lo_len, hi_len) + 1


class Test(unittest.TestCase):
    def test(self):
        self._test([1, 2, 2, 3, 1], 2)
        self._test([1, 2, 2, 3, 1, 4, 2], 6)

    def _test(self, nums, expected):
        actual = Solution().findShortestSubArray(nums)
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()
