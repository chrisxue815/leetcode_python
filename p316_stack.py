import unittest


class Solution(object):
    def removeDuplicateLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = map(ord, s)
        stack = []
        counts = [0] * (ord('z') + 1)
        visited = list(counts)

        for ch in s:
            counts[ch] += 1

        for ch in s:
            counts[ch] -= 1
            if visited[ch]:
                continue
            while stack and ch < stack[-1] and counts[stack[-1]]:
                visited[stack.pop()] = 0
            stack.append(ch)
            visited[ch] = 1

        return ''.join(chr(ch) for ch in stack)


class Test(unittest.TestCase):
    def test(self):
        self._test('bcab', 'bca')
        self._test('bcabc', 'abc')
        self._test('cbacdcbc', 'acdb')

    def _test(self, s, expected):
        actual = Solution().removeDuplicateLetters(s)
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()
