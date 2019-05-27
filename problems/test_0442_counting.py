import unittest


class Solution:
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        counts = [0] * (n + 1)

        for num in nums:
            counts[num] += 1

        duplicates = []
        for i in range(1, n + 1):
            if counts[i] == 2:
                duplicates.append(i)

        return duplicates


class Test(unittest.TestCase):
    def test(self):
        self._test([4, 3, 2, 7, 8, 2, 3, 1], [2, 3])

    def _test(self, nums, expected):
        actual = Solution().findDuplicates(nums)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
