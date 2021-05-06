import unittest

import utils


# O(n) time. O(n) space. Stack.
class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        buf = []
        k = 0

        for c in s:
            if c.isdigit():
                k = k * 10 + ord(c) - ord('0')
            elif c == '[':
                stack.append((buf, k))
                buf = []
                k = 0
            elif c == ']':
                sub = ''.join(buf)
                buf, k = stack.pop()
                buf.append(sub * k)
                k = 0
            else:
                buf.append(c)

        return ''.join(buf)


class Test(unittest.TestCase):
    def test(self):
        utils.test(self, __file__, Solution)


if __name__ == '__main__':
    unittest.main()
