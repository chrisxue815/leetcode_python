import unittest


class Solution(object):
    def findMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_len = 0
        sum_ = 0
        indices = {0: -1}
        for i, num in enumerate(nums):
            sum_ += 1 if num else -1
            index = indices.get(sum_, -2)
            if index != -2:
                length = i - index
                if length > max_len:
                    max_len = length
            else:
                indices[sum_] = i
        return max_len


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
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()
