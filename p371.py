import unittest


class Solution(object):
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        a &= 0xFFFFFFFF
        b &= 0xFFFFFFFF
        while b:
            a, b = a ^ b, (a & b) << 1

        a &= 0xFFFFFFFF
        if a & 0x80000000:
            a |= -0x80000000
        return a


class Test(unittest.TestCase):
    def test(self):
        for i in xrange(20):
            for j in xrange(20):
                self._test(i, j)

    def _test(self, a, b):
        self._test_arithmetic(a, b)
        self._test_arithmetic(b, a)

    def _test_arithmetic(self, a, b):
        self.assertEqual(Solution().getSum(a, b), a + b)
        self.assertEqual(Solution().getSum(a, -b), a - b)
        self.assertEqual(Solution().getSum(-a, b), -a + b)
        self.assertEqual(Solution().getSum(-a, -b), -a - b)


if __name__ == '__main__':
    unittest.main()