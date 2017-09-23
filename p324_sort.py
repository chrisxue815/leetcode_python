import unittest


# O(nlog(n)) time, O(n) space. Sorting, math
class Solution(object):
    def wiggleSort(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        aux = sorted(nums)

        i = 0
        hi = len(nums) - 1
        lo = half = hi >> 1

        while hi > half:
            nums[i] = aux[lo]
            nums[i + 1] = aux[hi]
            i += 2
            lo -= 1
            hi -= 1

        if lo >= 0:
            nums[i] = aux[lo]


class Test(unittest.TestCase):
    def test(self):
        self._test([1, 3, 2, 2, 3, 1])
        self._test([1, 2, 1, 2, 1, 1, 2, 2, 1])
        self._test([1, 5, 1, 1, 6, 4])
        self._test([1, 2, 2, 3])

    def _test(self, nums):
        Solution().wiggleSort(nums)

        prev = nums[0] + 1
        asc = False
        for num in nums:
            if asc:
                self.assertLess(prev, num)
            else:
                self.assertGreater(prev, num)
            prev = num
            asc = not asc


if __name__ == '__main__':
    unittest.main()
