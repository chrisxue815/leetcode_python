import unittest


def _permute(nums, result, n):
    if n == 1:
        result.append(list(nums))
    else:
        for i in xrange(n):
            _permute(nums, result, n - 1)

            if n & 1:
                nums[0], nums[n - 1] = nums[n - 1], nums[0]
            else:
                nums[i], nums[n - 1] = nums[n - 1], nums[i]


class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        _permute(nums, result, len(nums))
        return result


class Test(unittest.TestCase):
    def test(self):
        self._test([1, 2, 3], [
            [1, 2, 3],
            [1, 3, 2],
            [2, 1, 3],
            [2, 3, 1],
            [3, 1, 2],
            [3, 2, 1]
        ])

    def _test(self, nums, expected):
        actual = Solution().permute(nums)
        self.assertItemsEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()
