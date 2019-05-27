import unittest


class Solution:
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        duplicates = []

        for i in range(n):
            num = nums[i]
            if num <= 0:
                continue
            nums[i] = 0

            while True:
                next_num = nums[num - 1]
                if next_num < 0:
                    duplicates.append(num)
                    break
                elif next_num == 0:
                    nums[num - 1] = -1
                    break
                else:
                    nums[num - 1] = -1
                    num = next_num

        return duplicates


class Test(unittest.TestCase):
    def test(self):
        self._test([4, 3, 2, 7, 8, 2, 3, 1], [2, 3])
        self._test([2, 1], [])
        self._test([3, 3, 1], [3])
        self._test([1], [])
        self._test([1, 1], [1])
        self._test([2, 1, 1], [1])

    def _test(self, nums, expected):
        actual = Solution().findDuplicates(nums)
        self.assertCountEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
