import unittest


def _count_smaller_or_equal_numbers(num, matrix):
    count = 0
    for row in matrix:
        lo = 0
        hi = len(row) - 1

        while lo <= hi:
            mid = lo + ((hi - lo) >> 1)
            if row[mid] <= num:
                lo = mid + 1
            else:
                hi = mid - 1
        count += lo

    return count


# O(nlog(n)log(n^2)) time. O(1) space. Binary search.
class Solution(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        lo = matrix[0][0]
        hi = matrix[-1][-1]

        while lo <= hi:
            mid = lo + ((hi - lo) >> 1)
            count = _count_smaller_or_equal_numbers(mid, matrix)
            if count < k:
                lo = mid + 1
            else:
                hi = mid - 1
        return lo


class Test(unittest.TestCase):
    def test(self):
        self._test([
            [1, 5, 9],
            [10, 11, 13],
            [12, 13, 15]
        ], 8, 13)

        self._test([
            [1, 2],
            [3, 3],
        ], 2, 2)

        self._test([
            [1, 2],
            [1, 3],
        ], 2, 1)

        self._test([
            [1, 1],
            [1, 3],
        ], 3, 1)

        self._test([
            [2]
        ], 1, 2)

    def _test(self, matrix, k, expected):
        actual = Solution().kthSmallest(matrix, k)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
