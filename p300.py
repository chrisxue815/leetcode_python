import unittest


class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        last_item_in_sequence = []
        for i in nums:
            lo = 0
            hi = len(last_item_in_sequence) - 1
            while lo <= hi:
                mid = lo + ((hi - lo) >> 1)
                mid_val = last_item_in_sequence[mid]
                if mid_val < i:
                    lo = mid + 1
                elif mid_val > i:
                    hi = mid - 1
                else:
                    lo = mid
                    break
            if lo == len(last_item_in_sequence):
                last_item_in_sequence.append(i)
            else:
                last_item_in_sequence[lo] = i
        return len(last_item_in_sequence)


class Test(unittest.TestCase):
    def test(self):
        self._test([10, 9, 2, 5, 3, 7, 101, 18], 4)
        self._test([10, 9, 2, 8, 3, 7, 101, 18], 4)
        self._test([10, 9, 2, 8, 3, 7, 101, 101, 18], 4)

    def _test(self, nums, expected):
        actual = Solution().lengthOfLIS(nums)
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()
