import unittest


class Solution:
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        if not divisor:
            return float('inf')
        if not dividend:
            return 0
        if dividend == -0x80000000 and divisor == -1:
            return 0x7FFFFFFF

        pos = (dividend < 0) == (divisor < 0)
        if dividend < 0:
            dividend = -dividend
        if divisor < 0:
            divisor = -divisor

        result = 0
        for i in range(31, -1, -1):
            if dividend >> i >= divisor:
                dividend -= divisor << i
                result += 1 << i

        return result if pos else -result


class Test(unittest.TestCase):
    def test(self):
        for i in range(100):
            for j in range(1, 100):
                self._test(i, j, int(float(i) / j))

        self._test(1, 0, float('inf'))
        self._test(-0x80000000, -1, 0x7FFFFFFF)

    def _test(self, dividend, divisor, expected):
        actual = Solution().divide(dividend, divisor)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
