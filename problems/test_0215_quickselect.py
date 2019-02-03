import unittest


def partition(nums, lo, hi):
    pivot = nums[hi - 1]
    w = lo

    for r in range(lo, hi):
        if nums[r] > pivot:
            nums[r], nums[w] = nums[w], nums[r]
            w += 1

    nums[w], nums[hi - 1] = nums[hi - 1], nums[w]
    return w


def kth_largest(nums, lo, hi, k):
    pivot_index = partition(nums, lo, hi)
    if pivot_index > k:
        return kth_largest(nums, lo, pivot_index, k)
    elif pivot_index < k:
        return kth_largest(nums, pivot_index + 1, hi, k)
    else:
        return nums[pivot_index]


# Quickselect, O(1) space. Best case and average O(n), worst case O(n^2) time
class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        return kth_largest(nums, 0, len(nums), k - 1)


class Test(unittest.TestCase):
    def test(self):
        self._test([3, 2, 1, 5, 6, 4], 2, 5)
        self._test([0, 0], 2, 0)

    def _test(self, nums, k, expected):
        actual = Solution().findKthLargest(nums, k)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
