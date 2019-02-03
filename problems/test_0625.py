import unittest


class Solution(object):
    def smallestFactorization(self, a):
        """
        :type a: int
        :rtype: int
        """
        if a < 10:
            return a

        counts = [0] * 10
        for factor in range(9, 1, -1):
            while a != 1:
                q, r = divmod(a, factor)
                if r:
                    break
                counts[factor] += 1
                a = q
            else:
                break
        else:
            return 0

        result = 0
        for factor in range(2, 10):
            for _ in range(counts[factor]):
                # Note: how to check integer add and mul overflow in other languages
                result = result * 10 + factor

        return result if result < (1 << 31) else 0


class Test(unittest.TestCase):
    def test(self):
        self._test(48, 68)
        self._test(15, 35)
        self._test(1, 1)
        self._test(22, 0)

    def _test(self, a, expected):
        actual = Solution().smallestFactorization(a)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
