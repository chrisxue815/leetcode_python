import unittest

import utils


def dfs(s, i):
    buf = []
    k = 0
    while i < len(s):
        c = s[i]
        if c.isdigit():
            k = k * 10 + ord(c) - ord('0')
        elif c == '[':
            i, sub = dfs(s, i + 1)
            buf.append(sub * k)
            k = 0
        elif c == ']':
            break
        else:
            buf.append(c)
        i += 1

    return i, ''.join(buf)


# O(n) time. O(n) space. DFS.
class Solution:
    def decodeString(self, s: str) -> str:
        i, sub = dfs(s, 0)
        return sub


class Test(unittest.TestCase):
    def test(self):
        utils.test(self, __file__, Solution)


if __name__ == '__main__':
    unittest.main()
