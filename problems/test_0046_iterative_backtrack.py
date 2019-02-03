import unittest


class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        n = len(nums)
        result = []

        cycles = range(n)
        result.append(list(nums))

        while True:
            for i in xrange(n - 1, -1, -1):
                cycles[i] += 1
                j = cycles[i]

                if j < n:
                    nums[i], nums[j] = nums[j], nums[i]
                    result.append(list(nums))
                    break
                else:
                    cycles[i] = i
                    nums[i:] = nums[i + 1:] + [nums[i]]
            else:
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
        self.assertItemsEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
