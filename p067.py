import unittest

_offset = ord('0') << 1


class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        result = []

        if len(a) < len(b):
            a, b = b, a

        carry = 0
        i = len(a) - 1

        for j in xrange(len(b) - 1, -1, -1):
            digit = ord(a[i]) + ord(b[j]) + carry - _offset
            if digit >= 2:
                digit -= 2
                carry = 1
            else:
                carry = 0
            result.append(str(digit))
            i -= 1

        for i in xrange(i, -1, -1):
            digit = ord(a[i]) + carry - ord('0')
            if digit == 2:
                digit = 0
                carry = 1
            else:
                carry = 0
            result.append(str(digit))

        if carry:
            result.append('1')

        return ''.join(reversed(result))


class Test(unittest.TestCase):
    def test(self):
        self._test('11', '1', '100')

    def _test(self, a, b, expected):
        actual = Solution().addBinary(a, b)
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()
