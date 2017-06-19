import unittest


class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        if len(num1) < len(num2):
            num1, num2 = num2, num1

        result = []
        carry = 0
        i1 = len(num1) - 1
        i2 = len(num2) - 1
        for i in xrange(len(num2)):
            digit = carry + ord(num1[i1]) + ord(num2[i2]) - ord('0') * 2
            if digit >= 10:
                digit -= 10
                carry = 1
            else:
                carry = 0
            result.append(digit)
            i1 -= 1
            i2 -= 1

        for i in xrange(len(num1) - len(num2) - 1, -1, -1):
            digit = carry + ord(num1[i]) - ord('0')
            if digit >= 10:
                digit -= 10
                carry = 1
            else:
                carry = 0
            result.append(digit)

        if carry:
            result.append(carry)

        return ''.join(chr(digit + ord('0')) for digit in reversed(result))


class Test(unittest.TestCase):
    def test(self):
        self._test('123', '123', '246')
        self._test('1123', '123', '1246')
        self._test('123', '1123', '1246')
        self._test('1', '999', '1000')

    def _test(self, num1, num2, expected):
        actual = Solution().addStrings(num1, num2)
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()
