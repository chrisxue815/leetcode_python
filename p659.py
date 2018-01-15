import unittest
import heapq


class Solution(object):
    def isPossible(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if not nums:
            return False

        curr_num = nums[0]
        curr_queue = []
        next_queue = []

        for num in nums:
            if num != curr_num:
                if num > curr_num + 1:
                    if next_queue and next_queue[0] < 3:
                        return False
                    next_queue = []
                if curr_queue and curr_queue[0] < 3:
                    return False
                curr_num = num
                curr_queue = next_queue
                next_queue = []

            count = heapq.heappop(curr_queue) if curr_queue else 0
            heapq.heappush(next_queue, count + 1)

        return (not curr_queue or curr_queue[0] >= 3) and (not next_queue or next_queue[0] >= 3)


class Test(unittest.TestCase):
    def test(self):
        self._test([1, 2, 3, 3, 4, 5], True)
        self._test([1, 2, 3, 3, 4, 4, 5, 5], True)
        self._test([1, 2, 3, 4, 4, 5], False)
        self._test([1, 3, 4, 5], False)

    def _test(self, nums, expected):
        actual = Solution().isPossible(nums)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
