import unittest


class Solution:
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        prev = [1]
        for i in range(1, rowIndex + 1):
            row = [1] * (i + 1)
            for j in range(1, i):
                row[j] = prev[j - 1] + prev[j]
            prev = row
        return prev


class Test(unittest.TestCase):
    def test(self):
        self._test(0, [1])
        self._test(1, [1, 1])
        self._test(2, [1, 2, 1])
        self._test(3, [1, 3, 3, 1])

    def _test(self, rowIndex, expected):
        actual = Solution().getRow(rowIndex)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
