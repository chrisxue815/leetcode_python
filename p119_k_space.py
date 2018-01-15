import unittest


class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        row = [1] * (rowIndex + 1)
        for i in xrange(2, rowIndex + 1):
            prev = 1
            for j in xrange(1, i):
                curr = row[j]
                row[j] = curr + prev
                prev = curr
        return row


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
