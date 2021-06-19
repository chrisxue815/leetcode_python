import unittest

import utils


class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        if not k:
            return num
        n = len(num)
        stack = []
        for i in range(n):
            digit = num[i]
            while k and stack and ord(digit) < ord(stack[-1]):
                stack.pop()
                k -= 1
            stack.append(digit)
        hi = len(stack) - k
        lo = 0
        while lo < hi and stack[lo] == '0':
            lo += 1
        return ''.join(stack[lo:hi]) if lo < hi else '0'


class Test(unittest.TestCase):
    def test(self):
        utils.test(self, __file__, Solution)


if __name__ == '__main__':
    unittest.main()
