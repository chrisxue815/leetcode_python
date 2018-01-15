import unittest


# O(n) time. O(1) space.
class Solution(object):
    def dominantIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        largest = -0x80000000
        largest_index = -1
        for i, num in enumerate(nums):
            if num > largest:
                largest = num
                largest_index = i
        half = largest // 2
        return largest_index if all(num <= half or num == largest for num in nums) else -1


class Test(unittest.TestCase):
    def test(self):
        cases = [
            ([3, 6, 1, 0], 1),
            ([1, 2, 3, 4], -1),
        ]

        for case in cases:
            actual = Solution().dominantIndex(*case[:-1])
            self.assertEqual(case[-1], actual)


if __name__ == '__main__':
    unittest.main()
