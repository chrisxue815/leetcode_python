import unittest

_zero = ord('0')


def _to_array(num):
    arr = [0] * len(num)
    i = len(num) - 1
    for ch in num:
        arr[i] = ord(ch) - _zero
        i -= 1
    return arr


def _mul(num1, num2, index):
    product = [0] * index
    factor = num2[index]
    carry = 0

    for digit in num1:
        p = digit * factor + carry
        carry = p // 10
        product.append(p - carry * 10)

    if carry != 0:
        product.append(carry)

    return product


def _add(num1, num2):
    carry = 0
    for i in xrange(len(num1)):
        sum_ = num1[i] + num2[i] + carry
        if sum_ >= 10:
            carry = 1
            sum_ -= 10
        else:
            carry = 0

        num1[i] = sum_

    for i in xrange(len(num1), len(num2)):
        sum_ = num2[i] + carry
        if sum_ >= 10:
            carry = 1
            sum_ -= 10
        else:
            carry = 0

        num1.append(sum_)

    if carry != 0:
        num1.append(carry)


class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        num1 = _to_array(num1)
        num2 = _to_array(num2)

        product = []

        for i in xrange(len(num2)):
            p = _mul(num1, num2, i)
            _add(product, p)

        while len(product) > 1 and product[-1] == 0:
            product.pop()

        product.reverse()
        return ''.join(str(digit) for digit in product)


class Test(unittest.TestCase):
    def test(self):
        self._test('1234', '5678', str(1234 * 5678))
        self._test('1234', '567', str(1234 * 567))
        self._test('123', '5678', str(123 * 5678))
        self._test('9', '9', str(9 * 9))
        self._test('0', '9', str(0 * 9))

    def _test(self, num1, num2, expected):
        actual = Solution().multiply(num1, num2)
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()
