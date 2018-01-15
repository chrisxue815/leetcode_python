import unittest


# O(n) time. O(1) space.
class Solution(object):
    def dominantIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        largest = second_largest = -0x80000000
        largest_index = -1

        for i, num in enumerate(nums):
            if num >= largest:
                second_largest = largest
                largest = num
                largest_index = i
            elif num > second_largest:
                second_largest = num

        return largest_index if largest >= second_largest * 2 else -1


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
