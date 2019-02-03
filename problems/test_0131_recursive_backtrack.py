import unittest


class Solution(object):
    def __init__(self):
        self.s = None
        self.n = 0
        self.combination = []
        self.result = []

    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        self.s = s
        self.n = len(s)

        self._partition(0, 0)

        return self.result

    def _partition(self, lo, hi):
        if hi == self.n:
            if lo == hi:
                self.result.append(list(self.combination))
        else:
            i = lo
            j = hi
            while i < j:
                if self.s[i] != self.s[j]:
                    break
                i += 1
                j -= 1
            else:
                self.combination.append(self.s[lo:hi + 1])
                self._partition(hi + 1, hi + 1)
                self.combination.pop()

            self._partition(lo, hi + 1)


class Test(unittest.TestCase):
    def test(self):
        self._test("aab", [
            ["a", "a", "b"],
            ["aa", "b"],
        ])

        self._test("aba", [
            ["a", "b", "a"],
            ["aba"],
        ])

        self._test("abba", [
            ["a", "b", "b", "a"],
            ["a", "bb", "a"],
            ["abba"],
        ])

        self._test("abbab", [
            ["a", "b", "b", "a", "b"],
            ["a", "bb", "a", "b"],
            ["a", "b", "bab"],
            ["abba", "b"],
        ])

    def _test(self, s, expected):
        actual = Solution().partition(s)
        self.assertItemsEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
