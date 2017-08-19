import unittest


class Window(object):
    def __init__(self):
        self.gaps = 0
        self.indices = []


class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        if len(s) <= k:
            return len(s)

        result = 0
        windows = [Window() for _ in xrange(26)]

        for i, ch in enumerate(s):
            window = windows[ord(ch) - ord('A')]
            indices = window.indices

            if indices:
                window.gaps += i - indices[-1] - 1

            window.indices.append(i)

            while window.gaps > k:
                left = indices.pop(0)
                window.gaps -= indices[0] - left - 1
            result = max(result, indices[-1] - indices[0] + 1 + k - window.gaps)

        return min(result, len(s))


class Test(unittest.TestCase):
    def test(self):
        self._test('ABAB', 2, 4)
        self._test('AABABBA', 1, 4)
        self._test('AAAA', 5, 4)
        self._test('AAAA', 2, 4)

    def _test(self, s, k, expected):
        actual = Solution().characterReplacement(s, k)
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()
