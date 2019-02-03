import itertools
import unittest


class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        result = [[]]
        for num in nums:
            num_permutations = len(result)
            for i in range(num_permutations):
                permutation = result[i]
                for j in range(len(permutation)):
                    if permutation[j] == num:
                        permutation.insert(j, num)
                        break
                    clone = list(permutation)
                    clone.insert(j, num)
                    result.append(clone)
                else:
                    permutation.append(num)
        return result


class Test(unittest.TestCase):
    def test(self):
        self._test([1, 1, 2])
        self._test([1, 2, 3])
        self._test([0, 1, 0, 0, 9])

    def _test(self, nums):
        actual = Solution().permuteUnique(nums)
        self.assertCountEqual([list(p) for p in set(p for p in itertools.permutations(nums))], actual)


if __name__ == '__main__':
    unittest.main()
