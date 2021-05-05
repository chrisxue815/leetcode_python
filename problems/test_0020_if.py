import unittest

import utils


# O(n) time. O(n) space. Stack.
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for c in s:
            if c == '(' or c == '[' or c == '{':
                stack.append(c)
            elif c == ')':
                if not stack or stack.pop() != '(':
                    return False
            elif c == ']':
                if not stack or stack.pop() != '[':
                    return False
            elif c == '}':
                if not stack or stack.pop() != '{':
                    return False

        return len(stack) == 0


class Test(unittest.TestCase):
    def test(self):
        utils.test(self, __file__, Solution)


if __name__ == '__main__':
    unittest.main()
