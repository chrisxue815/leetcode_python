import unittest

import utils


def dfs(s, i):
    result = 0
    num = 0
    sign = 1

    while i < len(s):
        c = s[i]
        if c.isdigit():
            num = num * 10 + ord(c) - ord('0')
        elif c == '+' or c == '-':
            result += num * sign
            num = 0
            sign = 44 - ord(c)  # '+' == 43, '-' == 45
        elif c == '(':
            i, addend = dfs(s, i + 1)
            result += addend * sign
        elif c == ')':
            break
        i += 1

    return i, result + num * sign


# O(n) time. O(n) space. DFS.
class Solution:
    def calculate(self, s: str) -> int:
        i, result = dfs(s, 0)
        return result


class Test(unittest.TestCase):
    def test(self):
        utils.test(self, __file__, Solution)


if __name__ == '__main__':
    unittest.main()
