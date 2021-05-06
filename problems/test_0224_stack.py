import unittest

import utils


# O(n) time. O(n) space. Stack.
class Solution:
    def calculate(self, s: str) -> int:
        result = 0
        stack = []
        num = 0
        sign = 1

        for c in s:
            if c.isdigit():
                num = num * 10 + ord(c) - ord('0')
            elif c == '+' or c == '-':
                result += num * sign
                num = 0
                sign = 44 - ord(c)
            elif c == '(':
                stack.append((result, sign))
                result = 0
                sign = 1
            elif c == ')':
                addend = result + num * sign
                num = 0
                result, sign = stack.pop()
                result += addend * sign

        return result + num * sign


class Test(unittest.TestCase):
    def test(self):
        utils.test(self, __file__, Solution)


if __name__ == '__main__':
    unittest.main()
