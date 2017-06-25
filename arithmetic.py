import unittest


def add(a, b):
    a &= 0xFFFFFFFF
    b &= 0xFFFFFFFF

    while b:
        a, b = a ^ b, ((a & b) << 1)

    if a & 0x80000000:
        a |= -0x80000000
    else:
        a &= 0xFFFFFFFF

    return a


def sub(a, b):
    return add(a, add(~b, 1))


def mul(a, b):
    if not a or not b:
        return 0
    if a == 1:
        return b
    if b == 1:
        return a

    pos = (a < 0) == (b < 0)
    if a < 0:
        a = -a
    if b < 0:
        b = - b

    result = 0
    while b != 1:
        if b & 1:
            result += a
        a <<= 1
        b >>= 1
    result += a

    return result if pos else -result


class Test(unittest.TestCase):
    def test(self):
        for i in xrange(20):
            for j in xrange(20):
                self._test(i, j)

    def _test(self, a, b):
        self._test_arithmetic(a, b)
        self._test_arithmetic(a, -b)
        self._test_arithmetic(-a, b)
        self._test_arithmetic(-a, -b)

    def _test_arithmetic(self, a, b):
        self.assertEqual(add(a, b), a + b)
        self.assertEqual(add(b, a), b + a)

        self.assertEqual(sub(a, b), a - b)
        self.assertEqual(sub(b, a), b - a)

        self.assertEqual(mul(a, b), a * b)
        self.assertEqual(mul(b, a), b * a)


if __name__ == '__main__':
    unittest.main()
