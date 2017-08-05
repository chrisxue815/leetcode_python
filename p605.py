import unittest


class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        if n == 0:
            return True

        prev = -2
        for i, planted in enumerate(flowerbed):
            if planted:
                space = (i - prev - 2) >> 1
                if space > 0:
                    n -= space
                    if n <= 0:
                        return True
                prev = i

        space = (len(flowerbed) - prev - 1) >> 1
        if space > 0:
            n -= space
            if n <= 0:
                return True
        return False


class Test(unittest.TestCase):
    def test(self):
        self._test([1, 0, 0, 0, 1], 1, True)
        self._test([1, 0, 0, 0, 1], 2, False)
        self._test([1, 0, 0, 0, 1, 0, 0], 2, True)
        self._test([1], 0, True)
        self._test([0, 0, 1], 1, True)

    def _test(self, flowerbed, n, expected):
        actual = Solution().canPlaceFlowers(flowerbed, n)
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()
