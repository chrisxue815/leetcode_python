import unittest


def _separate_re_im(x):
    plus_index = x.index('+')
    re = int(x[:plus_index])
    im = int(x[plus_index + 1:-1])
    return re, im


class Solution(object):
    def complexNumberMultiply(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        (a_re, a_im) = _separate_re_im(a)
        (b_re, b_im) = _separate_re_im(b)
        c_re = a_re * b_re - a_im * b_im
        c_im = a_im * b_re + a_re * b_im
        return str(c_re) + '+' + str(c_im) + 'i'


class Test(unittest.TestCase):
    def test(self):
        self._test('1+1i', '1+1i', '0+2i')
        self._test('1+-1i', '1+-1i', '0+-2i')

    def _test(self, a, b, expected):
        actual = Solution().complexNumberMultiply(a, b)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
