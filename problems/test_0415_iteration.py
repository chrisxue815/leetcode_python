import unittest

import utils


# O(n) time. O(n) space. Iteration.
class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        if len(num1) < len(num2):
            num1, num2 = num2, num1

        result = []
        carry = 0

        for i in range(len(num1)):
            a = ord(num1[len(num1) - 1 - i]) - ord('0')
            b = ord(num2[len(num2) - 1 - i]) - ord('0') if i < len(num2) else 0
            c = a + b + carry
            if c >= 10:
                c -= 10
                carry = 1
            else:
                carry = 0
            result.append(str(c))

        if carry == 1:
            result.append('1')

        return ''.join(reversed(result))


class Test(unittest.TestCase):
    def test(self):
        utils.test(self, __file__, Solution)


if __name__ == '__main__':
    unittest.main()
