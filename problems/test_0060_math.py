import unittest


class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        k -= 1
        factorials = [1, 1, 2, 6, 24, 120, 720, 5040, 40320][:n]
        candidates = [1, 2, 3, 4, 5, 6, 7, 8, 9][:n]
        result = ''
        for factorial in reversed(factorials):
            index = k // factorial
            result += str(candidates[index])
            candidates.pop(index)
            k -= factorial * index
        return result


class Test(unittest.TestCase):
    def test(self):
        self._test(3, 5, '312')

    def _test(self, n, k, expected):
        actual = Solution().getPermutation(n, k)
        self.assertCountEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
