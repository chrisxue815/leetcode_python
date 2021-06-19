import unittest

import utils


# O(n) time. O(1) space. Stack.
class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        s = list(map(ord, s))
        stack = []
        counts = [0] * (ord('z') + 1)
        visited = [False] * (ord('z') + 1)

        for c in s:
            counts[c] += 1

        for c in s:
            counts[c] -= 1
            if visited[c]:
                continue
            while stack and c < stack[-1] and counts[stack[-1]]:
                visited[stack.pop()] = False
            stack.append(c)
            visited[c] = True

        return ''.join(map(chr, stack))


class Test(unittest.TestCase):
    def test(self):
        utils.test(self, __file__, Solution)


if __name__ == '__main__':
    unittest.main()
