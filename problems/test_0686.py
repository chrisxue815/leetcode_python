import unittest


# O(n)
class Solution:
    def repeatedStringMatch(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: int
        """
        if len(a) >= len(b):
            if b in a:
                return 1
            return 2 if b in a + a else -1

        lo = b.find(a)

        if lo == -1:
            return -1
        if not a.endswith(b[:lo]):
            return -1

        hi = lo + len(a)

        while hi + len(a) <= len(b):
            if not b.startswith(a, hi):
                return -1
            hi += len(a)

        if not a.startswith(b[hi:]):
            return -1

        return (hi - lo) // len(a) + (lo != 0) + (hi != len(b))


class Test(unittest.TestCase):
    def test(self):
        self._test('abcd', 'cdabcdab', 3)
        self._test('a', 'a', 1)
        self._test('aa', 'a', 1)
        self._test('a', 'aaaa', 4)
        self._test('abcd', 'cdab', 2)

    def _test(self, a, b, expected):
        actual = Solution().repeatedStringMatch(a, b)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
