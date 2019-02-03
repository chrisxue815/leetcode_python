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


def div(a, b):
    if not b:
        return float('inf')
    if not a:
        return 0

    pos = (a < 0) == (b < 0)
    if a < 0:
        a = -a
    if b < 0:
        b = - b

    result = 0
    for i in range(31, -1, -1):
        if a >> i >= b:
            result += 1 << i
            a -= b << i

    return result if pos else -result


class Test(unittest.TestCase):
    def test(self):
        for i in range(20):
            for j in range(20):
                self._test(i, j)

    def _test(self, a, b):
        self._test_arithmetic(a, b)
        self._test_arithmetic(a, -b)
        self._test_arithmetic(-a, b)
        self._test_arithmetic(-a, -b)

    def _test_arithmetic(self, a, b):
        self.assertEqual(a + b, add(a, b))
        self.assertEqual(b + a, add(b, a))

        self.assertEqual(a - b, sub(a, b))
        self.assertEqual(b - a, sub(b, a))

        self.assertEqual(a * b, mul(a, b))
        self.assertEqual(b * a, mul(b, a))

        if b:
            self.assertEqual(int(float(a) / b), div(a, b))
        if a:
            self.assertEqual(int(float(b) / a), div(b, a))


if __name__ == '__main__':
    unittest.main()
