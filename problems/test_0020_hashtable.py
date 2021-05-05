import unittest

import utils

open_brackets = ['(', '[', '{']
close_brackets = {
    ')': '(',
    ']': '[',
    '}': '{',
}


# O(n) time. O(n) space. Stack, hash table.
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for c in s:
            if c in open_brackets:
                stack.append(c)
            elif not stack or stack.pop() != close_brackets[c]:
                return False

        return len(stack) == 0


class Test(unittest.TestCase):
    def test(self):
        utils.test(self, __file__, Solution)


if __name__ == '__main__':
    unittest.main()
