import unittest


def gcd_euclid(a, b):
    if a == 0 or b == 0:
        return 0
    while b:
        a, b = b, a % b
    return a


def lcm_euclid(a, b):
    c = gcd_euclid(a, b)
    return a / c * b


def gcd_stein(a, b):
    if a == 0 or b == 0:
        return 0
    c = 1
    while True:
        if a == 0:
            return b * c
        if b == 0:
            return a * c
        if a & 1 == 0:
            if b & 1 == 0:
                a >>= 1
                b >>= 1
                c <<= 1
            else:
                a >>= 1
        else:
            if b & 1 == 0:
                b >>= 1
            else:
                a, b = abs(a - b), min(a, b)


class Test(unittest.TestCase):
    def test_gcd(self):
        self._test_gcd(3, 5, 1)
        self._test_gcd(4, 6, 2)
        self._test_gcd(9, 12, 3)
        self._test_gcd(9, 15, 3)
        self._test_gcd(0, 15, 0)

    def _test_gcd(self, a, b, gcd):
        self._test_gcd_euclid_stein(a, b, gcd)
        self._test_gcd_euclid_stein(b, a, gcd)

    def _test_gcd_euclid_stein(self, a, b, gcd):
        self.assertEqual(gcd, gcd_euclid(a, b))
        self.assertEqual(gcd, gcd_stein(a, b))


if __name__ == '__main__':
    unittest.main()
