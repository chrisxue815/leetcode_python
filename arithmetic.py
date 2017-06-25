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


if __name__ == '__main__':
    unittest.main()
