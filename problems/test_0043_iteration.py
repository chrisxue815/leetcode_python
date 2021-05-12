import unittest

import utils


def to_reversed_digits(num):
    return [ord(c) - ord('0') for c in reversed(num)]


# O(mn) time. O(m+n) space. Iteration.
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == '0' or num2 == '0':
            return '0'
        if num1 == '1':
            return num2
        if num2 == '1':
            return num1

        result = [0] * (len(num1) + len(num2))
        num1 = to_reversed_digits(num1)
        num2 = to_reversed_digits(num2)

        for i, a in enumerate(num1):
            for j, b in enumerate(num2):
                result[i + j] += a * b

        carry = 0
        for i, c in enumerate(result):
            c += carry
            result[i] = c % 10
            carry = c // 10

        while result[-1] == 0:
            result.pop()

        result.reverse()
        return ''.join(str(digit) for digit in result)


class Test(unittest.TestCase):
    def test(self):
        utils.test(self, __file__, Solution)


if __name__ == '__main__':
    unittest.main()
