import unittest


class Solution(object):
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        result = [0]
        for i in range(n):
            prefix = 1 << i
            for j in range(len(result) - 1, -1, -1):
                result.append(prefix + result[j])
        return result


class Test(unittest.TestCase):
    def test(self):
        self._test(0, [0])
        self._test(1, [0, 1])
        self._test(2, [0, 1, 3, 2])

    def _test(self, n, expected):
        actual = Solution().grayCode(n)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
