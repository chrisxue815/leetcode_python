import itertools
import unittest


class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        result = []
        self._permute(nums, result, 0)
        return result

    def _permute(self, nums, result, start):
        if start == len(nums):
            result.append(list(nums))
        else:
            next_index = start + 1
            self._permute(nums, result, next_index)

            for i in range(next_index, len(nums)):
                if nums[i] == nums[start]:
                    continue
                nums[i], nums[start] = nums[start], nums[i]
                self._permute(nums, result, next_index)

            nums[start:len(nums)] = nums[start + 1:len(nums)] + nums[start:start + 1]


class Test(unittest.TestCase):
    def test(self):
        self._test([1, 1, 2])
        self._test([1, 2, 3])
        self._test([0, 1, 0, 0, 9])

    def _test(self, nums):
        actual = Solution().permuteUnique(nums)
        self.assertItemsEqual([list(p) for p in set(p for p in itertools.permutations(nums))], actual)


if __name__ == '__main__':
    unittest.main()
