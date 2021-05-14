import unittest

import utils


# O(n) time. O(n) space. Stack, hash table.
class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        removed = set()
        for i, c in enumerate(s):
            if c == '(':
                stack.append(i)
            elif c == ')':
                if stack:
                    stack.pop()
                else:
                    removed.add(i)
        removed.update(stack)

        return ''.join(c for i, c in enumerate(s) if i not in removed)


class Test(unittest.TestCase):
    def test(self):
        utils.test(self, __file__, Solution)


if __name__ == '__main__':
    unittest.main()
