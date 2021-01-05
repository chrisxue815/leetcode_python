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
        cases = utils.load_test_json(__file__).test_cases

        for case in cases:
            args = str(case.args)
            actual = Solution().removeDuplicateLetters(**case.args.__dict__)
            self.assertEqual(case.expected, actual, msg=args)


if __name__ == '__main__':
    unittest.main()
