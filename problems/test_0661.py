import unittest


class Solution:
    def imageSmoother(self, m):
        """
        :type m: List[List[int]]
        :rtype: List[List[int]]
        """
        result = [None] * len(m)

        for i in range(len(m)):
            row = [0] * len(m[0])
            for j in range(len(row)):
                s = m[i][j]
                count = 1
                if i >= 1:
                    s += m[i - 1][j]
                    count += 1
                    if j >= 1:
                        s += m[i - 1][j - 1]
                        count += 1
                    if j + 1 < len(row):
                        s += m[i - 1][j + 1]
                        count += 1
                if i + 1 < len(m):
                    s += m[i + 1][j]
                    count += 1
                    if j >= 1:
                        s += m[i + 1][j - 1]
                        count += 1
                    if j + 1 < len(row):
                        s += m[i + 1][j + 1]
                        count += 1
                if j >= 1:
                    s += m[i][j - 1]
                    count += 1
                if j + 1 < len(row):
                    s += m[i][j + 1]
                    count += 1
                row[j] = s // count
            result[i] = row
        return result


class Test(unittest.TestCase):
    def test(self):
        self._test([
            [1, 1, 1],
            [1, 0, 1],
            [1, 1, 1]
        ], [
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]
        ])

    def _test(self, M, expected):
        actual = Solution().imageSmoother(M)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
