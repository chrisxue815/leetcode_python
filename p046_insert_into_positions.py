import unittest


class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = [[]]
        for num in nums:
            num_permutations = len(result)
            for i in xrange(num_permutations):
                permutation = result[i]
                for j in xrange(len(permutation)):
                    clone = list(permutation)
                    clone.insert(j, num)
                    result.append(clone)
                permutation.append(num)
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
