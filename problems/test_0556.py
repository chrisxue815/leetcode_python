import unittest


class Solution(object):
    def nextGreaterElement(self, n):
        """
        :type n: int
        :rtype: int
        """
        digits = []
        while n > 0:
            n, r = divmod(n, 10)
            digits.append(r)

        for i in range(1, len(digits)):
            if digits[i] < digits[i - 1]:
                break
        else:
            return -1

        for j in range(i):
            if digits[j] > digits[i]:
                break

        digits[i], digits[j] = digits[j], digits[i]

        digits[:i] = reversed(digits[:i])

        n = 0
        for digit in reversed(digits):
            n = n * 10 + digit

        if n >= 1 << 31:
            return -1

        return n


class Test(unittest.TestCase):
    def test(self):
        self._test(12, 21)
        self._test(21, -1)

        self._test(123, 132)
        self._test(132, 213)
        self._test(213, 231)
        self._test(231, 312)
        self._test(312, 321)
        self._test(321, -1)

        self._test(1233, 1323)

        self._test(2147483476, 2147483647)
        self._test(2147483486, -1)

    def _test(self, n, expected):
        actual = Solution().nextGreaterElement(n)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
