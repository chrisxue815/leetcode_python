import unittest


class Solution(object):
    def lexicalOrder(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        if n <= 9:
            return list(range(1, n + 1))

        result = []

        def add(base):
            for base in range(base, base + 10):
                if base > n:
                    return
                result.append(base)
                add(base * 10)

        for i in range(1, 10):
            result.append(i)
            add(i * 10)

        return result


class Test(unittest.TestCase):
    def test(self):
        self._test(13, [1, 10, 11, 12, 13, 2, 3, 4, 5, 6, 7, 8, 9])
        self._test(20, [1, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 2, 20, 3, 4, 5, 6, 7, 8, 9])

    def _test(self, n, expected):
        actual = Solution().lexicalOrder(n)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
