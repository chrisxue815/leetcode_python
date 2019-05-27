import unittest


def _permute(nums, result, n):
    n -= 1

    if n == 0:
        result.append(list(nums))
    else:
        for i in range(n):
            _permute(nums, result, n)

            if n & 1:
                nums[i], nums[n] = nums[n], nums[i]
            else:
                nums[0], nums[n] = nums[n], nums[0]

        _permute(nums, result, n)


class Solution:
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
        self.assertCountEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
