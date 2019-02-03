import unittest


def _to_roman(num, roman, radix, one, five, ten):
    if num < radix:
        return num, roman

    q = num // radix

    if q <= 3:
        roman += one * q
    elif q == 4:
        roman += one + five
    elif q == 5:
        roman += five
    elif q <= 8:
        roman += five + one * (q - 5)
    elif q == 9:
        roman += one + ten

    num -= radix * q

    return num, roman


class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        roman = ''

        (num, roman) = _to_roman(num, roman, 1000, 'M', '', '')
        (num, roman) = _to_roman(num, roman, 100, 'C', 'D', 'M')
        (num, roman) = _to_roman(num, roman, 10, 'X', 'L', 'C')
        (num, roman) = _to_roman(num, roman, 1, 'I', 'V', 'X')

        return roman


class Test(unittest.TestCase):
    def test(self):
        self._test(1, 'I')
        self._test(2, 'II')
        self._test(3, 'III')
        self._test(4, 'IV')
        self._test(5, 'V')
        self._test(6, 'VI')
        self._test(7, 'VII')
        self._test(8, 'VIII')
        self._test(9, 'IX')
        self._test(10, 'X')
        self._test(11, 'XI')
        self._test(12, 'XII')
        self._test(13, 'XIII')
        self._test(14, 'XIV')
        self._test(15, 'XV')
        self._test(16, 'XVI')
        self._test(17, 'XVII')
        self._test(18, 'XVIII')
        self._test(19, 'XIX')
        self._test(20, 'XX')
        self._test(21, 'XXI')
        self._test(30, 'XXX')
        self._test(35, 'XXXV')
        self._test(39, 'XXXIX')
        self._test(40, 'XL')
        self._test(50, 'L')
        self._test(100, 'C')
        self._test(500, 'D')
        self._test(1000, 'M')

    def _test(self, num, expected):
        actual = Solution().intToRoman(num)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
