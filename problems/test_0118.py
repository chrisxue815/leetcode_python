import unittest


class Solution:
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if not numRows:
            return []
        triangle = [[1] * i for i in range(1, numRows + 1)]

        for i in range(3, numRows + 1):
            prev = triangle[i - 2]
            curr = triangle[i - 1]

            for j in range(1, i - 1):
                curr[j] = prev[j - 1] + prev[j]

        return triangle


class Test(unittest.TestCase):
    def test(self):
        self._test(
            5,
            [
                [1],
                [1, 1],
                [1, 2, 1],
                [1, 3, 3, 1],
                [1, 4, 6, 4, 1],
            ]
        )

    def _test(self, numRows, expected):
        actual = Solution().generate(numRows)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
