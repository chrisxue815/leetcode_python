import unittest


def max_length(sums, lo, hi):
    sum_ = (sums[hi] - sums[lo]) << 1
    length = hi - lo
    if sum_ > length:
        more = 1
    elif sum_ < length:
        more = 0
    else:
        return length
    if sums[lo] == more:
        return max_length(sums, lo + 1, hi)
    elif sums[hi] == more:
        return max_length(sums, lo, hi - 1)
    else:
        return max(max_length(sums, lo + 1, hi), max_length(sums, lo, hi - 1))


class Solution:
    def findMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        sums = [0] * (n + 1)
        sum_ = 0
        for i in range(n):
            sum_ += nums[i]
            sums[i + 1] = sum_
        return max_length(sums, 0, n)


class Test(unittest.TestCase):
    def test(self):
        self._test([0, 1], 2)
        self._test([0, 1, 0], 2)
        self._test([1, 1, 0, 1, 0], 4)
        self._test([1, 0, 1, 0, 1], 4)
        self._test([0, 1, 1, 0, 1], 4)
        self._test([0, 1, 1, 1, 1, 0, 0], 4)
        self._test([0, 1, 1, 1, 0], 2)
        self._test([0, 1, 0, 0, 1, 1, 1, 1, 0], 6)
        self._test([0, 1, 1, 1, 1, 0, 0, 1, 0], 6)

    def _test(self, nums, expected):
        actual = Solution().findMaxLength(nums)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
