import unittest


class Solution(object):
    def matrixReshape(self, nums, r, c):
        """
        :type nums: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        if not nums or len(nums) * len(nums[0]) != r * c:
            return nums

        width = len(nums[0])
        i = j = 0

        result = []
        for _ in range(r):
            row = []
            r = c
            while width - j < r:
                row += nums[i][j:]
                r -= width - j
                i += 1
                j = 0
            row += nums[i][j:j + r]
            j += r
            result.append(row)

        return result


class Test(unittest.TestCase):
    def test(self):
        self._test(
            [
                [1, 2],
                [3, 4],
            ],
            1, 4,
            [
                [1, 2, 3, 4],
            ])
        self._test(
            [
                [1, 2],
                [3, 4],
            ],
            2, 4,
            [
                [1, 2],
                [3, 4],
            ])

    def _test(self, nums, r, c, expected):
        actual = Solution().matrixReshape(nums, r, c)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
