import unittest

_zero = ord('0')


def _to_array(num):
    arr = [0] * len(num)
    i = len(num) - 1
    for ch in num:
        arr[i] = ord(ch) - _zero
        i -= 1
    return arr


class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        n1 = len(num1)
        n2 = len(num2)
        if n1 + n2 < 10:
            return str(int(num1) * int(num2))

        if num1 == '0' or num2 == '0':
            return '0'
        if num1 == '1':
            return num2
        if num2 == '1':
            return num1

        num1 = _to_array(num1)
        num2 = _to_array(num2)

        product = [0] * (n1 + n2)

        for i in xrange(n1):
            for j in xrange(n2):
                product[i + j] += num1[i] * num2[j]

        carry = 0
        for i in xrange(len(product)):
            num = product[i] + carry
            carry, product[i] = divmod(num, 10)

        while product[-1] == 0:
            product.pop()

        product.reverse()
        return ''.join(str(digit) for digit in product)


class Test(unittest.TestCase):
    def test(self):
        self._test('1234', '5678', str(1234 * 5678))
        self._test('1234', '567', str(1234 * 567))
        self._test('123', '5678', str(123 * 5678))
        self._test('9', '9', '81')
        self._test('0', '9', '0')

        self._test('9999999999', '0', '0')
        self._test('1000000000', '1000000000', '1000000000000000000')

    def _test(self, num1, num2, expected):
        actual = Solution().multiply(num1, num2)
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()
